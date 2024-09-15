from django.contrib import admin
from .models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'created_at', 'updated_at',)
    search_fields = ('title',)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created_at',)
    search_fields = ('title',)

