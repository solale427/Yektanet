from django.contrib import admin

# Register your models here.

from .models import Ad
from .models import Advertiser

admin.site.register(Ad)
admin.site.register(Advertiser)