# Generated by Django 4.1 on 2022-11-25 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0070_withdraw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdraw',
            name='fund',
        ),
        migrations.AddField(
            model_name='withdraw',
            name='typeF',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.typefunds', verbose_name='Tipo de fondo'),
            preserve_default=False,
        ),
    ]
