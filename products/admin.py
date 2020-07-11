from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
# Display order in admin panel
# These could be in any order and the display order would change
# Make sure new classes are registered below.
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
#sort by sku. This is a tuple because multiple sorts could be added eg 'category', 'name'. To reverse it, put a minus in front of sku.
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
