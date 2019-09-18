from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_405_METHOD_NOT_ALLOWED)
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .tokens import account_activation_token
from .serializers import AccountSerializer
from .permissions import (OwnAccount, AnonymousUser)

Accounts = get_user_model()


class AccountViewSet(ModelViewSet):
    permission_classes = (AnonymousUser|(IsAuthenticated & (OwnAccount|IsAdminUser)),)

    def create(self, request, *args, **kwargs):
        account = Accounts.objects.create_user (
            email=request.data['email'], password=request.data['password'], is_admin=request.data.get('admin', False), 
            firstName=request.data.get('firstName', ''), lastName=request.data.get('lastName', '')
        )

        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            current_site = get_current_site(request)
            to_email = account.email
            message = render_to_string('acc_active_email.html', {
                'account':account, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(account.pk)).decode(),
                'ofType': urlsafe_base64_encode(force_bytes('active')).decode(),
                'token': account_activation_token.make_token(account),
            })
            mail_subject = 'Activate Your Account.'
            Accounts.email_user(subject=mail_subject, message=message, to=[to_email]) 
            return Response('Check Your Email For Activation Link', status=HTTP_201_CREATED)
            # return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Method \"PUT\" not allowed."}, status=HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        self.get_object()
        account = Accounts.objects.get(id=kwargs['pk'])

        # If password and email registration then Send link for authentication
        current_site = get_current_site(request)
        if request.data.get('password', False):
            message = render_to_string('acc_reset_credentials.html', {
                'account':account, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(account.pk)).decode(),
                'ofType': urlsafe_base64_encode(force_bytes('r_password')).decode(),
                'data': urlsafe_base64_encode(force_bytes(request.data['password'])).decode(),
                'token': account_activation_token.make_token(account),
            })

        elif request.data.get('email', False):
            message = render_to_string('acc_reset_credentials.html', {
                'account':account, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(account.pk)).decode(),
                'ofType': urlsafe_base64_encode(force_bytes('r_email')).decode(),
                'data': urlsafe_base64_encode(force_bytes(request.data['email'])).decode(),
                'token': account_activation_token.make_token(account),
            })

        
        mail_subject = 'Reset Credentials.'
        to_email = account.email
        Accounts.email_user(subject=mail_subject, message=message, to=[to_email]) 
        return Response('Check Your Mail For Reset Link', status=HTTP_200_OK)
        
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


class Authenticate(View):
    account = None
    uid = 0
    ofType = None

    def activate(self, request, *args, **kwargs):
        self.account.active = True
        self.account.save()

    def resetEmail(self, request, *args, **kwargs):
        self.account.email = Accounts.objects.normalize_email(force_text(urlsafe_base64_decode(kwargs['data'])))
        self.account.save()

    def resetPassword(self, request, *args, **kwargs):
        self.account.set_password(force_text(urlsafe_base64_decode(kwargs['data'])))
        print(force_text(urlsafe_base64_decode(kwargs['data'])))
        self.account.save()

    def get(self, request, *args, **kwargs):
        try:
            self.uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            self.account = Accounts.objects.get(pk=self.uid)
            self.ofType = force_text(urlsafe_base64_decode(kwargs['ofType']))
        except(TypeError, ValueError, OverflowError, Accounts.DoesNotExist):
            self.account = None
        if self.account is not None and account_activation_token.check_token(self.account, kwargs['token']):

            if self.ofType == 'active':
                self.activate(request, *args, **kwargs)

            elif self.ofType == 'r_email':
                self.resetEmail(request, *args, **kwargs)

            elif self.ofType == 'r_password':
                self.resetPassword(request, *args, **kwargs)

        return redirect('/login/')
