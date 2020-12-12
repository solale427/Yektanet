from django.urls import path

from user_management.views import LoginView

app_name = 'user_management'
urlpatterns = [
    path('advertiser/login/', LoginView.as_view())
]
