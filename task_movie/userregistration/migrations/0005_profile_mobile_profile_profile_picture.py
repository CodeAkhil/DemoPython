# Generated by Django 4.2.13 on 2024-05-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userregistration', '0004_rename_bio_profile_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='dp'),
        ),
    ]
