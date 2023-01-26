from django.contrib import admin
# Import the models
from .models import Post

# Register your models here.
admin.site.register(Post)