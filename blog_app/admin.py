from django.contrib import admin
# Import the models
from .models import Post

# Register your models here.
# admin.site.register(Post)

# Customize the admin site
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']