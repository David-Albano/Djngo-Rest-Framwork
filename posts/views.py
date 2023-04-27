from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status, generics
from posts.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from posts.permission import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, fmt=None):
    return Response({
        'users': reverse('user-list', request=request, format=fmt),
        'posts': reverse('post-list', request=request, format=fmt)
    })


class UserList(generics.ListAPIView):
    # This two attributes names must like this always from these kind class
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    # This two attributes names must like this always from these kind class
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    # This two attributes names must like this always from these kind class
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # This two attributes names must like this always from these kind class
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    