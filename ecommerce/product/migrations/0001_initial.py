# Generated by Django 4.2.7 on 2023-12-11 11:11

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("desc", models.TextField(blank=True, null=True)),
                ("type", models.BooleanField(default=False)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Brand",
                        to="product.brand",
                    ),
                ),
                (
                    "category",
                    mptt.fields.TreeForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Category",
                        to="product.category",
                    ),
                ),
            ],
        ),
    ]
