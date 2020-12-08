from django.db.models import Subquery, F, OuterRef, Avg, DurationField
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic.base import RedirectView, View
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from user_management.models import Advertiser
from .models import Click, AdView
from .models import Ad
from .serializers.ad import AdSerializer


class BaseView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "base_template.html"
    process_ip = True

    def get(self, request):
        queryset = Advertiser.objects.all()
        return Response({'advertisers': queryset})


class ClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    process_ip = True

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.new_click(ad, self.request.user_ip)
        return ad.link


class AdViewSet(viewsets.ModelViewSet):

    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):
        super(AdViewSet, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/advertiser_management/')

    def perform_create(self, serializer):
        advertiser = get_object_or_404(Advertiser, username=self.request.data.get('advertiser_username',False))
        serializer.save(advertiser=advertiser)


class ClicksView(View):
    def get(self, request):
        return JsonResponse(list(Click.get_clicks_sum_per_hour()), safe=False)


class AdViewsView(View):
    def get(self, request):
        return JsonResponse(list(AdView.get_views_sum_per_hour()), safe=False)


class RatioView(View):
    def get(self, request):
        clicks_per_hour = Click.get_clicks_sum_per_hour()
        views_per_hour = AdView.get_views_sum_per_hour()

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
