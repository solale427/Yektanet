from django.urls import path

from . import views

app_name = 'advertiser_management'
urlpatterns = [
    path('', views.base_view),
    path('click/<int:pk>/', views.AdView.as_view())
]
