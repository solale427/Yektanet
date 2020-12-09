from rest_framework import permissions

from user_management.models import Advertiser


class IsAdvertiser(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            return bool( Advertiser.objects.all().filter(username=request.user.username).exists())
        except:
            return False
