# Generated by Django 4.1 on 2022-11-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0099_rename_tot_cierrecaja_aperbank_impor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cierrecaja',
            name='informcaja',
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='close_informcaja',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='monto de cierre informado caja'),
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='qper_informcaja',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='monto de apertura informado caja'),
        ),
    ]