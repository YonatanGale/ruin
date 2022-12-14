# Generated by Django 4.1 on 2022-10-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0015_alter_buy_uni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='cant',
            field=models.IntegerField(default=0, verbose_name='Unidades'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='uni',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Cantidad en Litros, kg o unidad'),
        ),
    ]
