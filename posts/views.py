from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.serializers import PostSerializer

@api_view(['GET', 'POST'])
def posts_list(request, format=None):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_serialized = PostSerializer(posts, many=True)
        return Response(posts_serialized.data)
    
    elif request.method == 'POST':
        post_data_serialized = PostSerializer(data=request.data)

        if post_data_serialized.is_valid():
            post_data_serialized.save()
            return Response(posts_serialized.data, status=status.HTTP_201_CREATED)

        return Response(posts_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def posts_details(request, post_id, format=None):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        post_serialized = PostSerializer(post)
        return Response(post_serialized.data)
    
    elif request.method == 'PUT':
        post_data_serialized = PostSerializer(post, data=request.data)
        
        if post_data_serialized.is_valid():
            post_data_serialized.save()
            return Response(post_data_serialized.data)
        
        return Response(post_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
