from django.contrib import admin

# Register your models here.

from .models import Ad
from .models import Advertiser


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_filter = ('approved',)
    search_fields = ['title']


admin.site.register(Advertiser)
