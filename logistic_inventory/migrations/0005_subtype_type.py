# Generated by Django 5.1.1 on 2024-09-12 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic_inventory', '0004_subtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtype',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='logistic_inventory.type'),
        ),
    ]