# Generated by Django 4.1 on 2022-10-29 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0019_alter_category_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='desc',
        ),
    ]
