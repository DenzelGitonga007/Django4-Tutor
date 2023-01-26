from django.contrib import admin
# Import the models
from .models import Post

# Register your models here.
# admin.site.register(Post)

# Customize the admin site
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # More customization
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)} #autocomplete slug field
    raw_id_fields = ['author'] # to search for users
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']