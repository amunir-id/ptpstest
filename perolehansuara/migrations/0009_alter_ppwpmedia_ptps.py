# Generated by Django 5.0 on 2024-02-05 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_alter_userpengawastps_userprofile'),
        ('perolehansuara', '0008_rename_uploadppwp_ppwpmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ppwpmedia',
            name='ptps',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
        ),
    ]