from django.contrib import admin
from webapp.models import Article, Tag


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']
    list_display_links = ['title']
    list_filter = ['author']
    search_fields = ['title', 'content']
    # fields = ['id', 'title', 'author', 'content', 'created_at', 'updated_at']
    exclude = []
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
