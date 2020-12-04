from django.urls import path

from . import views

app_name = 'advertiser_management'
urlpatterns = [
    path('', views.BaseView.as_view()),
    path('click/<int:pk>/', views.AdView.as_view()),
    path('new_ad/', views.AdView.new_add, name='new_add'),
]
