# Generated by Django 4.1 on 2022-09-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0011_alter_buy_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='mot',
        ),
        migrations.AddField(
            model_name='buy',
            name='cant',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='buy',
            name='name',
            field=models.CharField(default=1, max_length=150, verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]