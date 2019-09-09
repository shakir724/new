# Generated by Django 2.2.4 on 2019-08-28 15:58

from django.db import migrations, models
import validators


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20190828_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overview',
            name='googleAnalytic',
            field=models.CharField(max_length=128, validators=[validators.validateUrl, validators.validateSite]),
        ),
        migrations.AlterField(
            model_name='overview',
            name='siteName',
            field=models.CharField(max_length=50, validators=[validators.validateChar]),
        ),
    ]
