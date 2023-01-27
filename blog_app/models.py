from django.db import models
# Import timezone
from django.utils import timezone
# Import User model
from django.contrib.auth.models import User


# Query sets
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)
# Create your models here.
# Post model
class Post(models.Model):
    # Add status field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft' # choice, lable
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250) # title of the post, VARCHAR
    slug = models.SlugField(max_length=250) # short lable, VARCHAR
    # Creating the relationship
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # Continuation
    body = models.TextField() # body, TEXT
    # Datetime fields.
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Status
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    # Defining the sort order

    # Still the query set
    objects = models.Manager() # The default manager.
    published = PublishedManager() # The custom manager. 
    class Meta:
        ordering = ['-publish'] # order by the publishing field
        # Setup the index
        indexes = [
            models.Index(fields=['-publish']),
        ]


    def __str__(self): # return human readable representation of the object
        return self.title
