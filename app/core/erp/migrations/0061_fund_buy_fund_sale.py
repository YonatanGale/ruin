# Generated by Django 4.1 on 2022-11-24 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0060_cierrecaja_methodpay_typefunds_fund'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='buy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.buy', verbose_name='Compras'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fund',
            name='sale',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.sale', verbose_name='Ventas'),
            preserve_default=False,
        ),
    ]