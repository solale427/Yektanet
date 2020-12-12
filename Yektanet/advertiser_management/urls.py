from django.urls import path
from advertiser_management.views import AdViewSet, ClickRedirectView, ClicksView, \
    AdViewsView, RatioView, ViewToClickDurationView, BaseView, AdStatisticsDetail

app_name = 'advertiser_management'
urlpatterns = [
    path('', BaseView.as_view()),
    path('click/<int:pk>/', ClickRedirectView.as_view()),
    path('ad/', AdViewSet.as_view({
        'post': 'create'
    })),
    path('details/', AdStatisticsDetail.as_view()),
    path('details/clicks/sum/', ClicksView.as_view()),
    path('details/views/sum/', AdViewsView.as_view()),
    path('details/clicks/ratio/', RatioView.as_view()),
    path('details/clicks/duration/', ViewToClickDurationView.as_view()),
]
