from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_405_METHOD_NOT_ALLOWED)
from rest_framework.permissions import IsAdminUser

from django.shortcuts import get_object_or_404

from .models import Accounts
from .serializers import AccountSerializer
from .permissions import (OwnAccount, AnonymousUser)

class AccountViewSet(ModelViewSet):
    permission_classes = (OwnAccount|AnonymousUser|IsAdminUser,)

    def create(self, request, *args, **kwargs):
        account = Accounts.objects.create_user(email=request.data['email'], password=request.data['password'], is_admin=request.data.get('admin', False), firstName=request.data.get('firstName', ''), lastName=request.data.get('lastName', ''))

        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Method \"PUT\" not allowed."}, status=HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        self.get_object()
        account = Accounts.objects.get(id=kwargs['pk'])

        if request.data.get('password', False):
            account.set_password(request.data['password'])

        account.email = (Accounts.objects.normalize_email(request.data.get('email', account.email)))
        account.firstName = request.data.get('firstName', account.firstName)
        account.lastName = request.data.get('lastName', account.lastName)
        account.admin = request.data.get('admin', account.admin)
        account.save()

        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.admin:
                return Accounts.objects.all()
        return Accounts.objects.filter(id=self.request.user.id)

    serializer_class = AccountSerializer