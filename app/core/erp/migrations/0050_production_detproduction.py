# Generated by Django 4.1 on 2022-11-22 11:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0049_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('produc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
            ],
            options={
                'verbose_name': 'Pruduccion',
                'verbose_name_plural': 'Producciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Cantidad')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.materials')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.production')),
            ],
            options={
                'verbose_name': 'Detalle de produccion',
                'verbose_name_plural': 'Detalle de producciones',
                'ordering': ['id'],
            },
        ),
    ]
