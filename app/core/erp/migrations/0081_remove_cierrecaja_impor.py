# Generated by Django 4.1 on 2022-11-26 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0080_alter_cierrecaja_tot_alter_cierrecaja_typef'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cierrecaja',
            name='impor',
        ),
    ]