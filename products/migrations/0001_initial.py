# Generated by Django 4.2.4 on 2023-08-31 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                (
                    "custom_code",
                    models.PositiveIntegerField(verbose_name="Custom Product Code"),
                ),
                ("description", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                ("name", models.CharField(max_length=150)),
                (
                    "hscode",
                    models.CharField(
                        max_length=15, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "product_type",
                    models.CharField(
                        choices=[("Product", "Product"), ("Service", "Service")],
                        default="Product",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Year",
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
                ("year", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
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
                ("quantity", models.IntegerField(verbose_name="Quantity (KG)")),
                (
                    "dollar_value",
                    models.PositiveBigIntegerField(verbose_name="US Dollar Value"),
                ),
                (
                    "shillings_value",
                    models.PositiveBigIntegerField(verbose_name="UG Shillings Value"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
                (
                    "year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.year"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.productcategory",
            ),
        ),
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=50)),
                (
                    "trade_choice",
                    models.CharField(
                        choices=[
                            ("Import From", "Import From"),
                            ("Export To", "Export To"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "trade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.trade"
                    ),
                ),
            ],
        ),
    ]
