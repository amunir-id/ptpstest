# Generated by Django 5.0 on 2024-01-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wilayah', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kecamatan',
            old_name='dapilkabkota',
            new_name='dapil_kabkota',
        ),
        migrations.RemoveField(
            model_name='kecamatan',
            name='provinsi',
        ),
        migrations.AddField(
            model_name='kabkota',
            name='dapil_dprdkabkota',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kabkota',
            name='dapil_dprdprov',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provinsi',
            name='dapil_dpr',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provinsi',
            name='dapil_dprdprov',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
