# Generated by Django 4.2.7 on 2023-12-11 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_product_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="desc",
            new_name="description",
        ),
        migrations.RemoveField(
            model_name="category",
            name="parent",
        ),
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Brand",
                to="product.brand",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Category",
                to="product.category",
            ),
        ),
    ]
