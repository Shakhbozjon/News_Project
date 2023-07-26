from django.contrib import admin
from .models import News, Category, Contact


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'publish_time', 'status']
    list_filter = ['created_time', 'publish_time', 'status']
    prepopulated_fields = {"slug": ['title',]}
    # date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



admin.site.register(Contact)

