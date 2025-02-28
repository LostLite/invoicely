# Generated by Django 5.1.6 on 2025-02-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_rename_calculation_method_invoice_vat_calculation_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='discount_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='vat_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
