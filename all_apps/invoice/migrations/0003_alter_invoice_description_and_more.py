# Generated by Django 5.1.6 on 2025-02-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_invoice_invoice_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
