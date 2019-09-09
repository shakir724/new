from django.db import models
from django.core.validators import validate_slug
from django.contrib.auth import get_user_model

from validators import (validateChar, validateNo) 

Accounts = get_user_model()


class Fonts(models.Model):
    fontName = models.CharField(max_length=128)
    font = models.FileField(upload_to='webpages/static/fonts/')

    def __str__(self):
        return self.fontName


class Themes(models.Model):
    themeName = models.CharField(max_length=128)
    theme = models.FileField(upload_to='webpages/static/themes/')

    def __str__(self):
        return self.themeName


class Webpages(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    groomName = models.CharField(max_length=128, validators=[validateChar])
    brideName = models.CharField(max_length=128, validators=[validateChar])
    groomFamilyName = models.CharField(max_length=64, validators=[validateChar])
    brideFamilyName = models.CharField(max_length=64, validators=[validateChar])
    dateTime = models.DateTimeField()
    venue = models.CharField(max_length=256, validators=[validate_slug])
    font = models.ForeignKey(Fonts, on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey(Themes, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.groomName + ' Weds ' + self.brideName


class WebpageImages(models.Model):
    webpage = models.ForeignKey(Webpages, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='webpages/images/')

    def __str__(self):
        return self.webpage


class WebpageVideos(models.Model):
    webpage = models.ForeignKey(Webpages, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='webpages/videos/')

    def __str__(self):
        return self.webpage


class ToDoList(models.Model):
    webpage = models.ForeignKey(Webpages, on_delete=models.CASCADE)
    note = models.CharField(max_length=64, validators=[validateChar])
    priority = models.PositiveSmallIntegerField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.webpage


class GuestList(models.Model):
    webpage = models.ForeignKey(Webpages, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, validators=[validateChar])
    phone = models.CharField(max_length=10, validators=[validateNo])

    def __str__(self):
        return self.webpage

