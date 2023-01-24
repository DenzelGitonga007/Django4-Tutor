from django.db import models
from django.utils import timezone

# Create your models here.
# Post model
class Post(models.Model):
    # Add status field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250) # title of the post, VARCHAR
    slug = models.SlugField(max_length=250) # short lable, VARCHAR
    body = models.TextField() # body, TEXT
    # Datetime fields.
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Status
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    # Defining the sort order
    class Meta:
        ordering = ['-publish'] # order by the publishing field
        # Setup the index
        indexes = [
            models.Index(fields=['-publish']),
        ]


    def __str__(self): # return human readable representation of the object
        return self.title
