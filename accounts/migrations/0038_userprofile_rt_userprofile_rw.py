# Generated by Django 5.0 on 2024-02-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_userprofile_alamat'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rw',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
