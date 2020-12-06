from django.urls import path

from . import views

app_name = 'advertiser_management'
urlpatterns = [
    path('', views.BaseView.as_view()),
    path('click/<int:pk>/', views.AdvertisementView.as_view()),
    path('new_ad/', views.AdvertisementView.new_add, name='new_add'),
    path('details/clicks_sum/',views.DetailsView.get_clicks_sum_per_hour)
]
