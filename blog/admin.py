from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "created_at",
        "views",
        "is_published",
        "is_featured",
    )
    list_editable = ("is_published", "is_featured")
    list_filter = ("is_featured", "is_published", "category")
    search_fields = ("title", "author", "content")
    actions = ["make_featured"]

    @admin.action(description="Seçilmiş et")
    
    def make_featured(self, request, queryset):
        queryset.update(is_featured=True)