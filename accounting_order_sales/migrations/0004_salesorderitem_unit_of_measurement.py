# Generated by Django 5.1.1 on 2024-09-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_order_sales', '0003_alter_salesorder_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorderitem',
            name='unit_of_measurement',
            field=models.CharField(default='UND', max_length=10),
        ),
    ]