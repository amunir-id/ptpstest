# Generated by Django 5.0 on 2024-02-05 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perolehansuara', '0010_alter_ppwpmedia_ptps'),
    ]

    operations = [
        migrations.CreateModel(
            name='CekPpwp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('media', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='perolehansuara.ppwpmedia')),
            ],
        ),
    ]