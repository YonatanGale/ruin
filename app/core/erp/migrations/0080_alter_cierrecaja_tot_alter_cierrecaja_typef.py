# Generated by Django 4.1 on 2022-11-25 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0079_remove_cierrecaja_banco_remove_cierrecaja_caja_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cierrecaja',
            name='tot',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='typeF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.typefunds'),
        ),
    ]
