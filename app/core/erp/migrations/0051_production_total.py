# Generated by Django 4.1 on 2022-11-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0050_production_detproduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
