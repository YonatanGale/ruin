# Generated by Django 4.1 on 2022-11-29 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0096_sale_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='estado',
        ),
    ]