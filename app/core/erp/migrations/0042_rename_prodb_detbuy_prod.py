# Generated by Django 4.1 on 2022-11-21 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0041_alter_product_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detbuy',
            old_name='prodb',
            new_name='prod',
        ),
    ]
