# Generated by Django 4.1 on 2022-11-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0040_rename_productbrut_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
    ]