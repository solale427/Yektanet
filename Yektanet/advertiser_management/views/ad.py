from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from advertiser.models import Advertiser
from advertiser.permissions import IsAdvertiser
from advertiser_management.models import Click, AdView
from advertiser_management.models import Ad
from advertiser_management.serializers.ad import AdSerializer


class ClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    process_ip = True

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.new_click(ad, self.request.user_ip)
        return ad.link


class AdViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = AdSerializer
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [
        IsAuthenticated,
        IsAdvertiser
    ]

    def create(self, request, *args, **kwargs):
        super(AdViewSet, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/advertiser_management/')

    def perform_create(self, serializer):
        serializer.save(advertiser=self.request.user.advertiser)
