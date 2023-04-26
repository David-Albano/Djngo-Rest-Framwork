from django.urls import path
from posts.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', posts_list),
    path('posts/<int:post_id>/', posts_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)