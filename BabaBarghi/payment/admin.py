from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class BrandAdmin(admin.ModelAdmin):
    pass