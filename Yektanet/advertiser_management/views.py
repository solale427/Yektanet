from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Advertiser, Click, View
from .models import Ad
from django.views.generic.base import RedirectView, TemplateView
from .forms import AdForm
from django.shortcuts import redirect
from datetime import datetime


def increase_views(user_ip):
    ads = Ad.objects.all()
    current_time = datetime.now()
    for ad in ads:
        view = View(time=current_time, ad=ad, user_ip=user_ip)
        view.save()


class BaseView(TemplateView):
    template_name = "base_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] = Advertiser.objects.all()
        increase_views(self.request.user_ip)
        return context


class AdView(RedirectView):
    permanent = False
    query_string = True
    ad = ''

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        current_time = datetime.now()
        click = Click(time=current_time, ad=ad, user_ip=self.request.user_ip)
        click.save()
        return ad.link

    def new_add(request):
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
