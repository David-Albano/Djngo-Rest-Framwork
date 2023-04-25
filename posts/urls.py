from django.urls import path
from posts.views import *

urlpatterns = [
    path('posts/', posts_list),
    path('posts/<int:post_id>/', posts_details)
]