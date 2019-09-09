from rest_framework.viewsets import ModelViewSet
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .models import (Webpages, WebpageImages, WebpageVideos, ToDoList, GuestList, Fonts, Themes)
from .permissions import (OwnWebpage, OwnMedia)
from .serializers import (
    WebpageSerializer, 
    WebpageImageSerializer, 
    WebpageVideoSerializer, 
    ToDoListSerializer, 
    GuestListSerializer, 
    FontSerializer, 
    ThemeSerializer
)

from permissions import ReadOnly


Accounts = get_user_model()


class WebpageViewSet(ModelViewSet):
    def partial_update(self, request, *args, **kwargs):
        self.get_object()
        return super().partial_update(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.admin:
            return Webpages.objects.all()
        return Webpages.objects.filter(account__pk=self.request.user.id)

    serializer_class = WebpageSerializer
    permission_classes = (IsAuthenticated, IsAdminUser|OwnWebpage,)


class WebpageImageViewSet(ModelViewSet):
    def partial_update(self, request, *args, **kwargs):
        self.get_object()
        return super().partial_update(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.admin:
            return WebpageImages.objects.all()
        webpage = Webpages.objects.get(account__pk=self.request.user.id)
        return WebpageImages.objects.filter(webpage=webpage)

    serializer_class = WebpageImageSerializer
    permission_classes = (IsAuthenticated, IsAdminUser|OwnMedia)


class WebpageVideoViewSet(ModelViewSet):
    def partial_update(self, request, *args, **kwargs):
        self.get_object()
        return super().partial_update(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.admin:
            return WebpageVideos.objects.all()
        webpage = Webpages.objects.get(account__pk=self.request.user.id)
        return WebpageVideos.objects.filter(webpage=webpage)

    serializer_class = WebpageVideoSerializer
    permission_classes = (IsAuthenticated, IsAdminUser|OwnMedia)


class ToDoListViewSet(ModelViewSet):
    def partial_update(self, request, *args, **kwargs):
        self.get_object()
        return super().partial_update(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.admin:
            return ToDoList.objects.all()
        webpage = Webpages.objects.get(account__pk=self.request.user.id)
        return ToDoList.objects.filter(webpage=webpage)

    serializer_class = ToDoListSerializer
    permission_classes = (IsAuthenticated, IsAdminUser|OwnMedia,)


class GuestListViewSet(ModelViewSet):    
    def partial_update(self, request, *args, **kwargs):
        self.get_object()
        return super().partial_update(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.admin:
            return GuestList.objects.all()
        webpage = Webpages.objects.get(account__pk=self.request.user.id)
        return GuestList.objects.filter(webpage=webpage)

    serializer_class = GuestListSerializer
    permission_classes = (IsAuthenticated, IsAdminUser|OwnMedia,)
    

class FontViewSet(ModelViewSet):
    queryset = Fonts.objects.all()    
    serializer_class = FontSerializer
    permission_classes = (IsAdminUser|ReadOnly,)


class ThemeViewSet(ModelViewSet):    
    queryset = Themes.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = (IsAdminUser|ReadOnly,)
