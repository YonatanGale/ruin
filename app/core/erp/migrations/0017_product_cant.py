# Generated by Django 4.1 on 2022-10-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0016_alter_buy_cant_alter_buy_uni'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cant',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
    ]