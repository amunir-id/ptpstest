# Generated by Django 5.0 on 2024-02-04 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_alter_endreport_user_alter_startreport_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endreport',
            old_name='user',
            new_name='ptps',
        ),
        migrations.RenameField(
            model_name='startreport',
            old_name='user',
            new_name='ptps',
        ),
        migrations.RenameField(
            model_name='whetherreport',
            old_name='user',
            new_name='ptps',
        ),
    ]