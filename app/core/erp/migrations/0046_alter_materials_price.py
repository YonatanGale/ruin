# Generated by Django 4.1 on 2022-11-22 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0045_remove_materials_uni_alter_categorymaterials_unity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Precio de compra'),
        ),
    ]
