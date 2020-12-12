from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from advertiser.models import Advertiser


class IsAdvertiser(permissions.BasePermission, IsAuthenticated):

    def has_permission(self, request, view):
        if super(IsAdvertiser, self).has_permission():
            return bool(Advertiser.objects.all().filter(username=request.user.username).exists())
        else:
            return False
