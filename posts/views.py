from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.views import APIView
from django.http import Http404

class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        posts_serialized = PostSerializer(posts, many=True)
        return Response(posts_serialized.data)

    def post(self, request, format=None):
        post_data_serialized = PostSerializer(data=request.data)

        if post_data_serialized.is_valid():
            post_data_serialized.save()
            return Response(post_data_serialized.data, status=status.HTTP_201_CREATED)
    
        return Response(post_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    

class PostDetail(APIView):
    
    def get_post(self, post_id):
        try:
            return Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, post_id, format=None):
        post = self.get_post(post_id)
        post_serialized = PostSerializer(post)
        return Response(post_serialized.data)
    
    def put(self, request, post_id, format=None):
        post = self.get_post(post_id)
        post_data_serialized = PostSerializer(post, data=request.data)

        if post_data_serialized.is_valid():
            post_data_serialized.save()
            return Response(post_data_serialized.data)
    
        return Response(post_data_serialized.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, post_id, format=None):
        post = self.get_post(post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    