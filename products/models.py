from django.db import models
from django.conf import settings
from .utils import country_names

# Create your models here.
PRODUCT_TYPE = (
    ('Product', 'Product'),
    ('Service', 'Service')
)

TRADE_CHOICE = (
    ('Import From', 'Import From'),
    ('Export To', 'Export To')
)

class Year(models.Model):
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.year}"

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    hscode = models.CharField(max_length=15, unique=True, primary_key=True)
    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=20, default="Product")

    def __str__(self):
        return f"{self.name}: {self.product_type}"


class Product(models.Model):
    custom_code = models.CharField(max_length=20, verbose_name="Custom Product Code")
    description = models.CharField(max_length=150)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.description} -> {self.category.name}"

    def save(self, *args, **kwargs):
        self.custom_code = f"{self.category.hscode}{self.custom_code}"
        super().save(*args, **kwargs)


class Trade(models.Model):
    quantity = models.IntegerField(verbose_name="Quantity (KG)")
    dollar_value = models.PositiveBigIntegerField(verbose_name="US Dollar Value")
    shillings_value = models.PositiveBigIntegerField(verbose_name="UG Shillings Value")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    trade_choice = models.CharField(choices=TRADE_CHOICE, max_length=50)

    def __str__(self):
        return f"{self.product.description}: {self.trade_choice} -> {self.dollar_value}"

class Country(models.Model):
    name = models.CharField(max_length=50, choices=country_names)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trade.product.description}: {self.trade.trade_choice} ----> {self.name}"

# class TradeType(models.Model):
#     trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.trade.product.description}: {self.country.trade}: {self.country.name}"
    