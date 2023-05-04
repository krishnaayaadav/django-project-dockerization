from django.contrib import admin
from  .models import Product



@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')