# Generated by Django 4.1.7 on 2023-05-14 21:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_rename_craeted_message_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
