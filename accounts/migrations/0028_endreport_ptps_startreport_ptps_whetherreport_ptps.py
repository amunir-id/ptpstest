# Generated by Django 5.0 on 2024-02-04 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_remove_endreport_ptps_remove_startreport_ptps_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='endreport',
            name='ptps',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startreport',
            name='ptps',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whetherreport',
            name='ptps',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
            preserve_default=False,
        ),
    ]
