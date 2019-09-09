from rest_framework.serializers import ModelSerializer

from .models import (Overview, SocialMedia)


class OverviewSerializer(ModelSerializer):
    class Meta:
        model = Overview
        fields = '__all__'

class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'