from django.db import models

from validators import (validateChar, validateSite, validateUrl)

class Overview(models.Model):
    siteName = models.CharField(max_length=50, validators=[validateChar])
    siteAddress = models.CharField(max_length=50, validators=[validateUrl, validateSite])
    favIcon = models.ImageField(upload_to='settings/overview/')
    googleAnalytic = models.CharField(max_length=128, validators=[validateUrl, validateSite])

class SocialMedia(models.Model):
    facebook = models.CharField(null=True, max_length=50, validators=[validateUrl, validateSite])
    instagram = models.CharField(null=True, max_length=50, validators=[validateUrl, validateSite])
    tweeter = models.CharField(null=True, max_length=50, validators=[validateUrl, validateSite])
    snapchat = models.CharField(null=True, max_length=50, validators=[validateUrl, validateSite])
    pinterest = models.CharField(null=True, max_length=50, validators=[validateUrl, validateSite])
