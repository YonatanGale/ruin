# Generated by Django 4.1 on 2022-11-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0056_recycle_prod_alter_recycle_recy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recycle',
            name='cant',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Cantidad'),
        ),
    ]
