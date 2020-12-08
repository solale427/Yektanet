from rest_framework import permissions


class IsAdvertiser(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            return bool(not request.user.advertiser.is_deleted)
        except:
            return False
