from django.contrib import admin
from .models import Comment
from posts.models import Post

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
admin.site.register(Comment)
