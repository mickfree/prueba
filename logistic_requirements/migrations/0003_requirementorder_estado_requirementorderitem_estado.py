# Generated by Django 5.1.1 on 2024-09-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic_requirements', '0002_requirementorder_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementorder',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requirementorderitem',
            name='estado',
            field=models.CharField(choices=[('L', 'Listo'), ('P', 'Pendiente'), ('C', 'Comprando')], default='P', max_length=1),
        ),
    ]