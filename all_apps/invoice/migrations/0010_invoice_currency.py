# Generated by Django 5.1.6 on 2025-02-24 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_remove_invoice_vat_calculation_method'),
        ('settings', '0002_remove_currency_currently_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='currencies', to='settings.currency'),
        ),
    ]
