# Generated by Django 2.2.4 on 2019-08-27 17:31

from django.db import migrations, models
import validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='firstName',
            field=models.CharField(blank=True, max_length=16, validators=[validators.validateChar]),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='lastName',
            field=models.CharField(blank=True, max_length=16, validators=[validators.validateChar]),
        ),
    ]
