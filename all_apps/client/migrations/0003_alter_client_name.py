# Generated by Django 5.1.6 on 2025-02-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_rename_additional_info_client_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
