# Generated by Django 5.0 on 2024-02-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_userprofile_jk'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='alamat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
