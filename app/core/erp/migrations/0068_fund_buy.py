# Generated by Django 4.1 on 2022-11-25 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0067_remove_fund_payname_fund_methodpay'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='buy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.buy'),
        ),
    ]