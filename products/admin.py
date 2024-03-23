from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

admin.site.register(models.ProductModel, ProductAdmin)
admin.site.register(models.Review)
