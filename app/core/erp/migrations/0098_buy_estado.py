# Generated by Django 4.1 on 2022-11-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0097_remove_sale_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='estado',
            field=models.IntegerField(default=0),
        ),
    ]
