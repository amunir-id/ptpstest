# Generated by Django 5.0 on 2024-01-31 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laporanhasil', '0009_lhp_bentuk_lhp_tahapan_lhp_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lhp',
            name='user',
        ),
    ]
