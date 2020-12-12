from rest_framework import permissions

from advertiser.models import Advertiser


class IsAdvertiser(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            return bool(Advertiser.objects.all().filter(username=request.user.username).exists())
        except:
            return False
