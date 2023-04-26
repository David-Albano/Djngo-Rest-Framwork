from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status, mixins, generics

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    posts_queryset = Post.objects.all()
    posts_serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   

class PostDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    posts_queryset = Post.objects.all()
    posts_serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)   
    