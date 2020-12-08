from django.db.models import Count, Subquery, F, OuterRef, Avg, DurationField
from django.db.models.functions import TruncHour
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.views.generic.base import RedirectView, TemplateView, View

from .forms import AdForm
from .models import Advertiser, Click, AdView
from .models import Ad


class BaseView(TemplateView):
    template_name = "base_template.html"
    process_ip = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] = Advertiser.objects.all()
        AdView.increase_views(self.request.user_ip)
        return context


class ClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    process_ip = True

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.new_click(ad,self.request.user_ip)
        return ad.link


class CreateAdView(View):
    def post(self, request):
        form = AdForm(request.POST)
        if form.is_valid():
            advertiser = get_object_or_404(Advertiser, pk=int(form.cleaned_data['advertiser_id']))
            ad = Ad(title=form.cleaned_data['title'],
                    link=form.cleaned_data['link'],
                    image=form.cleaned_data['image'],
                    advertiser=advertiser
                    )
            ad.save()
            return redirect('/advertiser_management/')
        else:
            return HttpResponse(form.errors.as_ul())


class ClicksView(View):
    def get(self, request):
        return JsonResponse(list(Click.get_clicks_sum_per_hour()), safe=False)


class AdViewsView(View):
    def get(self, request):
        return JsonResponse(list(View.get_views_sum_per_hour()), safe=False)


class RatioView(View):
    def get(self, request):
        clicks_per_hour = Click.get_clicks_sum_per_hour()
        views_per_hour = View.get_views_sum_per_hour()

        click_statistics = {
            (click_data['ad'], click_data['hour']): click_data for click_data in clicks_per_hour
        }

        result = []
        for item in list(views_per_hour):
            views = item['views']
            clicks = click_statistics.get((item['ad'], item['hour']), {}).get('clicks', 0)
            result.append({
                'ratio': clicks / views,
                'ad_id': item['ad'],
                'hour': item['hour'],
            })

        result = sorted(result, key=lambda ratio_data: ratio_data['hour'])

        return JsonResponse(result, safe=False)


class ViewToClickDurationView(View):
    def get(self, request):
        duration_average = Click.objects.all().annotate(
            duration=Subquery(
                AdView.objects.filter(
                    ad_id=OuterRef('ad_id'),
                    user_ip=OuterRef('user_ip'),
                    time__lte=OuterRef('time'),
                ).annotate(
                    duration=OuterRef('time') - F('time')
                ).order_by('duration').values('duration')[:1],
            )
        ).aggregate(view_to_click_average=Avg('duration', output_field=DurationField()))['view_to_click_average']
        return JsonResponse(
            {
                'view_to_click_average': str(duration_average)
            }
        )
