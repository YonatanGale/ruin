# Generated by Django 4.1 on 2022-11-25 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0069_buy_methodpay_buy_typfund'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=150, verbose_name='Razon o motivo')),
                ('cant', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Monto')),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.fund')),
            ],
            options={
                'verbose_name': 'Retiro',
                'verbose_name_plural': 'Retiros',
                'ordering': ['id'],
            },
        ),
    ]
