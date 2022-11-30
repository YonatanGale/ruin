# Generated by Django 4.1 on 2022-11-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0098_buy_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cierrecaja',
            old_name='tot',
            new_name='aperbank_impor',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='typeF',
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='apercaja_impor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='closebank_impor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='closecaja_impor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='informcaja',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='monto informado caja'),
        ),
    ]