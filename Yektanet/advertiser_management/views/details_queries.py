from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.generics import ListAPIView

from advertiser_management.serializers import ClickSerializer, AdViewSerializer, ViewToClickSerializer
from advertiser_management.utils import get_clicks_to_views_ratio_per_hour, click_to_view_avg_duration
from advertiser_management.models import Click, AdView


class ClicksView(ListAPIView):
    queryset = Click.get_clicks_sum_per_hour()
    serializer_class = ClickSerializer


class AdViewsView(ListAPIView):
    queryset = AdView.get_views_sum_per_hour()
    serializer_class = AdViewSerializer


class RatioView(ListAPIView):
    queryset = get_clicks_to_views_ratio_per_hour()
    serializer_class = ViewToClickSerializer


class ViewToClickDurationView(ListAPIView):
    def get(self, request, *args, **kwargs):
        duration_average = click_to_view_avg_duration()
        return JsonResponse(
            {
                'view_to_click_average': str(duration_average)
            }
        )
