# Generated by Django 5.0 on 2024-02-07 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_alter_userpengawastps_user'),
        ('perolehansuara', '0014_alter_ppwpmedia_ptps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dpdrimedia',
            name='ptps',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dpdri', to='accounts.userpengawastps'),
        ),
        migrations.AlterField(
            model_name='dprdkabkotamedia',
            name='ptps',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dprdkabkota', to='accounts.userpengawastps'),
        ),
        migrations.AlterField(
            model_name='dprdprovmedia',
            name='ptps',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dprdprov', to='accounts.userpengawastps'),
        ),
        migrations.AlterField(
            model_name='dprrimedia',
            name='ptps',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dprri', to='accounts.userpengawastps'),
        ),
    ]
