# Generated by Django 4.1 on 2022-11-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0078_cierrecaja_banco_cierrecaja_caja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cierrecaja',
            name='banco',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='caja',
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='tot',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Monto de ciere'),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='impor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Monto informado'),
        ),
    ]
