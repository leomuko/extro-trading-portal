from django.contrib import admin

from .models import Product, Country, Year, Trade, ProductCategory
# Register your models here.
admin.site.register(Product)
admin.site.register(Country)
admin.site.register(Year)
admin.site.register(Trade)
# admin.site.register(TradeType)
admin.site.register(ProductCategory)