# Generated by Django 4.1 on 2022-11-19 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0032_buy_supplier_unity_productbrut_detbuy_buy_prov'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='dni',
            new_name='ci',
        ),
    ]