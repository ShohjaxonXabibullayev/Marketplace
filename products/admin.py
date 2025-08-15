from django.contrib import admin
from .models import Comment, Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', "date", 'category', 'author']
    inlines = [ProductImageInline]

admin.site.register(Comment)
admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
# Register your models here.
