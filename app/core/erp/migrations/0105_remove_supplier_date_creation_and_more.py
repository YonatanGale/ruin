# Generated by Django 4.1 on 2022-11-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0104_remove_supplier_user_create_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='date_creation',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user_creation1',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user_update1',
        ),
        migrations.AddField(
            model_name='supplier',
            name='user_create',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='user_update',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
