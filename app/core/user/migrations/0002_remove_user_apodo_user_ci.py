# Generated by Django 4.1 on 2022-11-19 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='apodo',
        ),
        migrations.AddField(
            model_name='user',
            name='ci',
            field=models.CharField(default=1, max_length=150, verbose_name='CI'),
            preserve_default=False,
        ),
    ]
