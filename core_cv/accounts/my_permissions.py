from rest_framework import permissions



class IsOwnerOrCommettee(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet. or admin
        return obj.user == request.user or not request.user.is_tenant() or request.user.is_superuser


class IsCommittee(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_tenant()


class UpdateTenant(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_tenant()


class MessageOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet. or admin
        return obj.author == request.user or not request.user.is_tenant() or request.user.is_superuser
