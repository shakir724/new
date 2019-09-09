from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED

from .serializers import (OverviewSerializer, SocialMediaSerializer)
from .models import (Overview, SocialMedia)

from permissions import ReadOnly


class OverviewViewSet(ModelViewSet):
    permission_classes = (IsAdminUser|ReadOnly,)
    
    serializer_class = OverviewSerializer 
    queryset = Overview.objects.all()

class SocialMediaViewSet(ModelViewSet):
    permission_classes = (IsAdminUser|ReadOnly,)

    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all() 
