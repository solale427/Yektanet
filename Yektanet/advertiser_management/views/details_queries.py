from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.generics import ListAPIView

from advertiser_management.serializers import ClickSerializer, AdViewSerializer, ViewToClickSerializer, \
    DetailsPerHourSerializer
from advertiser_management.utils import get_clicks_to_views_ratio_per_hour, click_to_view_avg_duration, \
    get_general_statistics
from advertiser_management.models import Click, AdView


class ClicksView(ListAPIView):
    serializer_class = ClickSerializer

    def get_queryset(self):
        return Click.get_clicks_sum_per_hour()


class AdViewsView(ListAPIView):
    serializer_class = AdViewSerializer

    def get_queryset(self):
        return AdView.get_views_sum_per_hour()


class RatioView(ListAPIView):
    serializer_class = ViewToClickSerializer

    def get_queryset(self):
        return get_clicks_to_views_ratio_per_hour()


class ViewToClickDurationView(ListAPIView):
    def get(self, request, *args, **kwargs):
        duration_average = click_to_view_avg_duration()
        return JsonResponse(
            {
                'view_to_click_average': str(duration_average)
            }
        )


class AdStatisticsDetail(ListAPIView):
    serializer_class = DetailsPerHourSerializer

    def get_queryset(self):
        return get_general_statistics()
