from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode

from .models import Product, Country, Year, Trade, ProductCategory
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("custom_code", "description", "show_category")
    list_filter = ("category__name", "description")
    search_fields = ("category__name", "custom_code")

    def show_category(self, obj):
        result = ProductCategory.objects.get(name=obj.category.name)
        return result.name

    show_category.short_description = "Product Category"

    class Meta:
        ordering = ("description", "custom_code")
    

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("show_trade", "show_trade_type","name")
    list_filter = ("name", "trade__product__description", "trade__trade_choice")
    search_fields = ("trade__product__description",)

    def show_trade(self, obj):
        trades = Trade.objects.get(id=obj.trade.id)
        return trades.product.description

    def show_trade_type(self, obj):
        trade_type = Trade.objects.get(id=obj.trade.id).trade_choice
        return trade_type

    show_trade.short_description = "Trade"
    show_trade_type.short_description = "Trade Type"

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    pass

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ("show_product", "show_category", "quantity", "dollar_value", "trade_choice", "show_country", "year")
    list_filter = ("product__description", "trade_choice","year__year")
    search_fields = ("product__description", "product__category__name")

    def show_product(self, obj):
        result = Product.objects.get(pk=obj.product.id)
        return result.description

    def show_country(self, obj):
        country = Country.objects.get(trade__id=obj.id)
        return country.name

    def show_category(self, obj):
        result = Product.objects.get(pk=obj.product.id).category.name
        return result

    show_product.short_description = "Product"
    show_country.short_description = "Country"
    show_category.short_description = "Product Category"

# admin.site.register(TradeType)
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("hscode", "name", "product_type")
    list_filter = ("name", "product_type")
    search_fields = ("name",)

    class Meta:
        ordering = ("hscode",)