from django.db.models import Count, Subquery, F, Max
from django.db.models.functions import TruncHour
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Advertiser, Click, AdView
from .models import Ad
from django.views.generic.base import RedirectView, TemplateView, View
from .forms import AdForm
from django.shortcuts import redirect
from datetime import datetime


def increase_views(user_ip):
    ads = Ad.objects.all()
    current_time = datetime.now()
    for ad in ads:
        AdView.objects.create(time=current_time, ad=ad, user_ip=user_ip)


class BaseView(TemplateView):
    template_name = "base_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] = Advertiser.objects.all()
        increase_views(self.request.user_ip)
        return context


class AdvertisementView(RedirectView):
    permanent = False
    query_string = True
    ad = ''

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        current_time = datetime.now()
        Click.objects.create(time=current_time, ad=ad, user_ip=self.request.user_ip)
        return ad.link

    def new_add(self, request):
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


class DetailsView(View):

    def get_clicks_sum_per_hour(self):
        clicks_per_hour = Click.objects.all().annotate(hour=TruncHour('time')).values('ad','hour').annotate(clicks=Count('id'))
        return HttpResponse(clicks_per_hour)

    def get_views_sum_per_hour(self):
        views_per_hour = AdView.objects.all().annotate(hour=TruncHour('time')).values('ad','hour').annotate(views=Count('id'))
        return HttpResponse(views_per_hour)

    def get_clicks_to_views_ratio(self):
        clicks_per_hour = Click.objects.all().annotate(hour=TruncHour('time')).values('ad','hour').annotate(clicks=Count('id'))
        views_per_hour = AdView.objects.all().annotate(hour=TruncHour('time')).values('ad','hour').annotate(views=Count('id'))
        for item in views_per_hour:
            item['ratio']=clicks_per_hour.filter(hour=item['hour']).count/item['views']

        views_per_hour.order_by('ratio')

    def get_view_duration_ave(self):
        views = AdView.objects.all()
        clicks = Click.objects.all().annotate(duration=Subquery(views.filter(user_ip=F('user_ip')).values('time').annotate(duration=TruncHour('time')-F('time')).annotate(max=Max('duration')).first()))





