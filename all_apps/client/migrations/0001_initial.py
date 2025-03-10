# Generated by Django 5.1.6 on 2025-02-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website_url', models.URLField()),
                ('phone', models.CharField(max_length=15)),
                ('additional_info', models.TextField()),
            ],
        ),
    ]
