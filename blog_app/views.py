from django.shortcuts import render
# Import the models
# Post model
from .models import Post
# For viewing a single post
from django.http import Http404

# Create your views here.
# Display/read/retrieve all the posts
def post_list(request):
    posts = Post.published.all()
    return render(request, 'templates/blog/post/list.html',
    {'posts': posts})
# Display a single post
def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    # Upon success
    return render(request,
    'templates/blog/post/detail.html',
    {'post': post})
    