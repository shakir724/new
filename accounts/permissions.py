from rest_framework.permissions import (BasePermission, SAFE_METHODS)

class OwnAccount(BasePermission):
    allowedMethods = ('PATCH', 'DELETE') + SAFE_METHODS
    def has_permission(self, request, view):
        if request.method in self.allowedMethods:
            if request.method == 'PATCH':
                return (not (request.data.get('admin', False)))
            return True
        return False


class AnonymousUser(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            if not request.user.is_authenticated:
                return True
        return False