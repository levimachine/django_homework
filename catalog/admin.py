from django.contrib import admin

from catalog.models import Category, Product, BlogPost, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price_per_piece', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'is_published')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'is_actual', 'product')
