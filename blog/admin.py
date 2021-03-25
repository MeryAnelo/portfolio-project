from django.contrib import admin
from .models import Blog, Category, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = Blog.list_display
    list_filter = Blog.list_filter
    search_fields = Blog.search_fields
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)