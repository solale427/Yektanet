from django.urls import path

from . import views

app_name = 'advertiser_management'
urlpatterns = [
    path('', views.BaseView.as_view()),
    path('click/<int:pk>/', views.ClickRedirectView.as_view()),
    path('new_ad/', views.CreateAdView.as_view()),
    path('details/clicks/sum/', views.ClicksView.as_view()),
    path('details/views/sum/', views.AdViewsView.as_view()),
    path('details/clicks/ratio/', views.RatioView.as_view()),
    path('details/clicks/duration/', views.ViewToClickDurationView.as_view()),
]
