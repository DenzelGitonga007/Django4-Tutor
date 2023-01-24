from django.db import models

# Create your models here.
# Post model
class Post(models.Model):
    title = models.CharField(max_length=250) # title of the post, VARCHAR
    slug = models.SlugField(max_length=250) # short lable, VARCHAR
    body = models.TextField() # body, TEXT

    def __str__(self): # return human readable representation of the object
        return self.title
