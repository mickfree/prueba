# Generated by Django 5.1.1 on 2024-09-17 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0010_merge_20240917_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget_items', to='budget.catalogitem'),
        ),
    ]