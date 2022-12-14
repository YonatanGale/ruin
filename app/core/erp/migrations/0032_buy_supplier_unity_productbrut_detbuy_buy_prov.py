# Generated by Django 4.1 on 2022-11-19 08:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0031_delete_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='CI|RUC')),
                ('phone', models.CharField(max_length=10, unique=True, verbose_name='Telefono')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=150, unique=True, verbose_name='Unidad')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductBrut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('stock', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Stock')),
                ('pc', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de compra')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de creación')),
                ('uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.unity', verbose_name='Unidad')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetBuy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Cantidad')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.buy')),
                ('prodb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.productbrut')),
            ],
            options={
                'verbose_name': 'Detalle de Compra',
                'verbose_name_plural': 'Detalle de Compras',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='buy',
            name='prov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.supplier'),
        ),
    ]
