from django.urls import path

from user_management.views import AdvertiserLoginView

app_name = 'user_management'
urlpatterns = [
    path('advertiser/login/', AdvertiserLoginView.as_view())
]
