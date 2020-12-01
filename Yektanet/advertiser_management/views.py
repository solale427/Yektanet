from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Advertiser
from .models import Ad
from django.views.generic.base import RedirectView
from .forms import AdForm
from django.shortcuts import redirect


def base_view(request):
    advertisers = Advertiser.objects.all
    template = loader.get_template('base_template.html')
    context = {
        'advertisers': advertisers
    }
    return HttpResponse(template.render(context, request))


class AdView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.objects.all().filter(pk=kwargs['pk'])
        ad[0].increase_clicks()
        return ad[0].link


def new_add(request):
    form = AdForm(request.POST)
    if form.is_valid():
        advertiser = Advertiser.objects.all().filter(
                        pk=int(form.cleaned_data['advertiser_id'])
                        )[0]
        ad = Ad(title=form.cleaned_data['title'],
                link=form.cleaned_data['link'],
                image=form.cleaned_data['image'],
                advertiser=advertiser
                )
        ad.save()

    return redirect('/advertiser_management/')

