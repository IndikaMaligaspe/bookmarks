# Generated by Django 2.0.5 on 2020-04-16 04:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0002_auto_20200416_0931'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actions',
            new_name='Action',
        ),
    ]
