from rest_framework.serializers import ModelSerializer

from .models import (Webpages, WebpageImages, WebpageVideos, ToDoList, GuestList, Fonts, Themes)


class FontSerializer(ModelSerializer):
    class Meta:
        model = Fonts
        fields = '__all__'

class ThemeSerializer(ModelSerializer):
    class Meta:
        model = Themes
        fields = '__all__'

class WebpageSerializer(ModelSerializer):
    class Meta:
        model = Webpages
        fields = '__all__'

class WebpageImageSerializer(ModelSerializer):
    class Meta:
        model = WebpageImages
        fields = '__all__'

class WebpageVideoSerializer(ModelSerializer):
    class Meta:
        model = WebpageVideos
        fields = '__all__'

class ToDoListSerializer(ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'

class GuestListSerializer(ModelSerializer):
    class Meta:
        model = GuestList
        fields = '__all__'