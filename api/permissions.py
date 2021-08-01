from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwnerOrReadOnly(BasePermission):
    # user permissions
    def has_permission(self, request, view):
        ip_address = request.META['REMOTE_ADDR']
        in_blacklist = Blacklist.objects.filter(ip=ip_address).exists()

        return not in_blacklist

    # object permissions
    def has_object_permission(self, request, view, obj):
        # read only permission
        if request.method in permissions.SAFE_METHODS:  # safe methods are (get, head, )
            return True
        # update and delete permission for owner
        return request.user == obj.owner
