# Generated by Django 5.0 on 2024-02-07 05:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpengawastps',
            name='user',
            field=models.OneToOneField(limit_choices_to={'role': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
