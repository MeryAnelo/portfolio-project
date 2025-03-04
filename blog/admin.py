from django.contrib import admin
from .models import Blog, Category, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'publish_at','created_at','updated_at')
    search_fields = ['title','content']
    list_filter = ['status','publish_at','created_at']
    date_hierarchy = 'publish_at'
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-publish_at', '-created_at')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)