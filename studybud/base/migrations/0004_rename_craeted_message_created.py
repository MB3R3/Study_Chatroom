# Generated by Django 4.2 on 2023-05-14 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_rename_craeted_room_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='craeted',
            new_name='created',
        ),
    ]
