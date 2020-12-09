from django.db.models import Subquery, F, OuterRef, Avg, DurationField
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic.base import RedirectView, View
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from user_management.permissions import IsAdvertiser
from .utils import get_clicks_to_views_ratio_per_hour, click_to_view_avg_duration

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
        advertiser = get_object_or_404(Advertiser, username=self.request.data.get('advertiser_username', False))
        serializer.save(advertiser=advertiser)


class ClicksView(View):
    def get(self, request):
        return JsonResponse(list(Click.get_clicks_sum_per_hour()), safe=False)


class AdViewsView(View):
    def get(self, request):
        return JsonResponse(list(AdView.get_views_sum_per_hour()), safe=False)


class RatioView(View):
    def get(self, request):
        result = get_clicks_to_views_ratio_per_hour()
        return JsonResponse(result, safe=False)


class ViewToClickDurationView(View):
    def get(self, request):
        duration_average = click_to_view_avg_duration()
        return JsonResponse(
            {
                'view_to_click_average': str(duration_average)
            }
        )
