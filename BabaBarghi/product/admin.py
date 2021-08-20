from django.contrib import admin

from .models import Category, Price, Picture, Product, Brand
# Register your models here.

@admin.register(Category)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass

#########_____________________###########
# class ProductInline(admin.TabularInline):
#     model = Product
#     extra = 2
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [ProductInline]

#### Use ""modelAdmin.fiedset"" in your admin #########