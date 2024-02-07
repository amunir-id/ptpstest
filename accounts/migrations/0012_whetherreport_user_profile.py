# Generated by Django 5.0 on 2024-02-03 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_whetherreport_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='whetherreport',
            name='user_profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='accounts.userprofile'),
        ),
    ]