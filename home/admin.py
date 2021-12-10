from django.contrib import admin
from .models import Blog, Tag, Category

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'views', 'created_at']
    search_fields = ["title", 'views', "created_at"]
    list_per_page = 10


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ['name', 'slug', 'created_at']
    list_editable = ['slug']
    search_fields = ["name", 'slug', "created_at"]
    list_display_links = ['name']
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ["name", 'slug', "created_at"]
    list_per_page = 10
