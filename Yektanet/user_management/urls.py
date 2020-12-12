from django.urls import path

from user_management.views import LoginView, RegisterView, LogoutView

app_name = 'user_management'
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view())
]
