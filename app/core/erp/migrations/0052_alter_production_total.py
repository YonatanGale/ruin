# Generated by Django 4.1 on 2022-11-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0051_production_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
