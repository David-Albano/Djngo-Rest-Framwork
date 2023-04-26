from django.urls import path
from posts.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:post_id>/', PostDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)