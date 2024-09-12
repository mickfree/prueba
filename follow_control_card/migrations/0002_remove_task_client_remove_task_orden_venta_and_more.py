# Generated by Django 5.1.1 on 2024-09-12 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_order_sales', '0003_alter_salesorder_project'),
        ('follow_control_card', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='client',
        ),
        migrations.RemoveField(
            model_name='task',
            name='orden_venta',
        ),
        migrations.AddField(
            model_name='task',
            name='sale_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounting_order_sales.salesorder'),
            preserve_default=False,
        ),
    ]