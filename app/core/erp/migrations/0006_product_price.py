# Generated by Django 4.1 on 2022-08-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_alter_product_cate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Precio'),
        ),
    ]
