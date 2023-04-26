from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status, generics

class PostList(generics.ListCreateAPIView):
    # This attributes names must like this always from these kind class
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # This attributes names must like this always from these kind class
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    