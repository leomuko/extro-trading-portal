# Generated by Django 4.2.4 on 2023-09-11 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_remove_country_trade_choice_trade_trade_choice"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name_plural": "Countries"},
        ),
        migrations.AlterModelOptions(
            name="productcategory",
            options={"verbose_name_plural": "Product Categories"},
        ),
    ]