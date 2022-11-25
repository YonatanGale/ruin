# Generated by Django 4.1 on 2022-11-25 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0068_fund_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='methodpay',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.methodpay', verbose_name='Metodo de pago'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buy',
            name='typfund',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.typefunds'),
            preserve_default=False,
        ),
    ]