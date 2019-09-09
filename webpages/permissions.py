from rest_framework.permissions import (BasePermission, SAFE_METHODS)

from .models import Webpages

class OwnWebpage(BasePermission):
    def has_permission(self, request, view):
        allowedMethods = ('POST', 'PATCH', 'DELETE') + SAFE_METHODS

        if request.method in allowedMethods:
            # Restricts the User to Create And Update Webpage With Someone Else's Account Id
            if request.method in ('POST', 'PATCH'):
                return (request.data.get('account', str(request.user.id)) == str(request.user.id))

            return True
        return False


class OwnMedia(BasePermission):
    def has_permission(self, request, view):
        allowedMethods = ('POST', 'DELETE', 'PATCH') + SAFE_METHODS

        if request.method in allowedMethods:
            if request.method in ('POST', 'PATCH'):
                # Restricts the User to Create And Update Media on Someone Else's Webpage
                webpage = Webpages.objects.get(account=request.user)
                return (request.data.get('webpage', str(webpage.id)) == str(webpage.id))

            return True
        return False