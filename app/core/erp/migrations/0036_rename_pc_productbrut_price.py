# Generated by Django 4.1 on 2022-11-19 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0035_remove_unity_uname_unity_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productbrut',
            old_name='pc',
            new_name='price',
        ),
    ]
