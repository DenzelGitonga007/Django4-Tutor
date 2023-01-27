from django.urls import path
# Import the views
from . import views

app_name = 'blog_app'

urlpatterns = [
    #post views
    path('', views.post_list, name='post_list'), # diplay the list of posts
    path('<int:id>/', views.post_list, name='post_detail') # view a single post

]