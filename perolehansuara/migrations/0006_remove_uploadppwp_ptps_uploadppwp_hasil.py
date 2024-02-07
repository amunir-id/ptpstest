# Generated by Django 5.0 on 2024-02-05 01:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perolehansuara', '0005_remove_datadisabilitasppwp_tps_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadppwp',
            name='ptps',
        ),
        migrations.AddField(
            model_name='uploadppwp',
            name='hasil',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='perolehansuara.hasilppwp'),
        ),
    ]