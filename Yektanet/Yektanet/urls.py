from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advertiser_management/', include('advertiser_management.urls')),
    path('user_management/', include('user_management.urls'))
]
