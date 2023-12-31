# Generated by Django 4.2.7 on 2023-12-11 12:13

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_category_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Category",
                to="product.category",
            ),
        ),
    ]
