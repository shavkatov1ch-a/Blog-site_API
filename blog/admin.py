from django.contrib import admin
from .models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('title', 'created')


admin.site.register(Tag)