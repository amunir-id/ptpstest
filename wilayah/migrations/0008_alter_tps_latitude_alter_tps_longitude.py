# Generated by Django 5.0 on 2024-02-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wilayah', '0007_alter_tps_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tps',
            name='latitude',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tps',
            name='longitude',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
    ]
