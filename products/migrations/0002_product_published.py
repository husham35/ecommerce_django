# Generated by Django 5.1.2 on 2024-10-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="published",
            field=models.BooleanField(default=False),
        ),
    ]
