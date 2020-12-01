from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Advertiser
from .models import Ad
from django.views.generic.base import RedirectView


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
