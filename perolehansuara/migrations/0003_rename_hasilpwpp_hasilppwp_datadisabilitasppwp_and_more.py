# Generated by Django 5.0 on 2024-02-02 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perolehansuara', '0002_hasilpwpp'),
        ('wilayah', '0007_alter_tps_no'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HasilPwpp',
            new_name='HasilPpwp',
        ),
        migrations.CreateModel(
            name='DataDisabilitasPpwp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jml_lk', models.IntegerField(blank=True, default=0, null=True)),
                ('jml_pm', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.tps')),
            ],
        ),
        migrations.CreateModel(
            name='DataPemilihPenggunaHakPilihPpwp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datapemilih_lk', models.IntegerField(blank=True, default=0, null=True)),
                ('datapemilih_pm', models.IntegerField(blank=True, default=0, null=True)),
                ('pengguna_dpt_lk', models.IntegerField(blank=True, default=0, null=True)),
                ('pengguna_dpt_pm', models.IntegerField(blank=True, default=0, null=True)),
                ('pengguna_dptb_lk', models.IntegerField(blank=True, default=0, null=True)),
                ('pengguna_dptb_pm', models.IntegerField(blank=True, default=0, null=True)),
                ('pengguna_dpk_lk', models.IntegerField(blank=True, default=0, null=True)),
                ('pengguna_dpk_pm', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.tps')),
            ],
        ),
        migrations.CreateModel(
            name='DataPenggunaSuratSuaraPpwp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah_terima', models.IntegerField(blank=True, default=0, null=True)),
                ('jumlah_digunakan', models.IntegerField(blank=True, default=0, null=True)),
                ('jumlah_dikembalikan', models.IntegerField(blank=True, default=0, null=True)),
                ('jumlah_tidakdipakai', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.tps')),
            ],
        ),
        migrations.CreateModel(
            name='DataSuaraSahdanTidakSahPpwp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sah', models.IntegerField(blank=True, default=0, null=True)),
                ('tidak', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wilayah.tps')),
            ],
        ),
    ]