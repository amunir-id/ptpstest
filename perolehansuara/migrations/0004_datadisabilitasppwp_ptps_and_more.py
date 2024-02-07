# Generated by Django 5.0 on 2024-02-05 01:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_alter_userpengawastps_userprofile'),
        ('perolehansuara', '0003_rename_hasilpwpp_hasilppwp_datadisabilitasppwp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datadisabilitasppwp',
            name='ptps',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datapemilihpenggunahakpilihppwp',
            name='ptps',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datapenggunasuratsuarappwp',
            name='ptps',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datasuarasahdantidaksahppwp',
            name='ptps',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hasilppwp',
            name='ptps',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userpengawastps'),
            preserve_default=False,
        ),
    ]