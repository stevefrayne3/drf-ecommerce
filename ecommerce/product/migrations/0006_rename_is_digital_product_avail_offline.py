# Generated by Django 4.2.7 on 2023-12-11 12:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_rename_type_product_is_digital"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="is_digital",
            new_name="avail_offline",
        ),
    ]
