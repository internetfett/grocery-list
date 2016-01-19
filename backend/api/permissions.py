from rest_framework import permissions


class IsOwnerOrListing(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsRelatedOwnerOrListing(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object (via fkey) to edit it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        related_obj = getattr(obj, view.owner_related_field)
        return related_obj.user == request.user
