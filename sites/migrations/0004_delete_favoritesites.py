# Generated by Django 5.1.7 on 2025-03-23 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_favoritesites'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavoriteSites',
        ),
    ]
