# Generated by Django 5.0 on 2024-01-31 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laporanhasil', '0006_rename_post_lhpmedia_lhp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lhp',
            name='bentuk',
        ),
        migrations.RemoveField(
            model_name='lhp',
            name='sasaran',
        ),
        migrations.RemoveField(
            model_name='lhp',
            name='tahapan',
        ),
        migrations.RemoveField(
            model_name='lhp',
            name='tempat',
        ),
        migrations.RemoveField(
            model_name='lhp',
            name='uraian',
        ),
        migrations.RemoveField(
            model_name='lhp',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lhp',
            name='waktu',
        ),
    ]
