# Generated by Django 4.2.13 on 2024-05-25 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userregistration', '0003_rename_profession_profile_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='profession',
        ),
    ]