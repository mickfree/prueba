# Generated by Django 5.1.1 on 2024-09-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0011_alter_budgetitem_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogitem',
            old_name='name',
            new_name='sap',
        ),
    ]
