# Generated by Django 5.0 on 2024-02-04 06:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_userprofile_wa'),
        ('wilayah', '0014_alter_tps_lat_alter_tps_lng'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPengawasTps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kabkota', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.kabkota')),
                ('kecamatan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.kecamatan')),
                ('keldesa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.keldesa')),
                ('maker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maker', to=settings.AUTH_USER_MODEL)),
                ('provinsi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.provinsi')),
                ('tps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.tps')),
                ('user', models.OneToOneField(limit_choices_to={'role': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
