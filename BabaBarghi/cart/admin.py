from django.contrib import admin

from .models import Cart


@admin.register(Cart)
class BrandAdmin(admin.ModelAdmin):
    pass

#########_____________________###########
# class ProductInline(admin.TabularInline):
#     model = Product
#     extra = 2
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [ProductInline]

#### Use ""modelAdmin.fiedset"" in your admin #########