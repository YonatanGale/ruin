# Generated by Django 4.1 on 2022-11-29 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0103_remove_client_user_create_client_date_creation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='user_create',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user_update',
        ),
        migrations.AddField(
            model_name='supplier',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='user_creation1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_creation1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='supplier',
            name='user_update1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_update1', to=settings.AUTH_USER_MODEL),
        ),
    ]
