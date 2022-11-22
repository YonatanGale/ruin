# Generated by Django 4.1 on 2022-11-21 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0042_rename_prodb_detbuy_prod'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='materials',
            name='cate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.categorymaterials', verbose_name='Categoria'),
            preserve_default=False,
        ),
    ]