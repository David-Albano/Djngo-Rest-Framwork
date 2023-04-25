from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from posts.models import Post
from posts.serializers import PostSerializer

@csrf_exempt
def posts_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_serialized = PostSerializer(posts, many=True)
        return JsonResponse(posts_serialized.data, safe=False)
    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_data_serialized = PostSerializer(data=post_data)
        if post_data_serialized.is_valid():
            post_data_serialized.save()
            return JsonResponse(post_data_serialized.data, status=201)

        return JsonResponse(post_data_serialized.errors, status=400)
    

@csrf_exempt
def posts_details(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return HttpResponse(status=400)
    
    if request.method == 'GET':
        post_serialized = PostSerializer(post)
        return JsonResponse(post_serialized.data)
    elif request.method == 'PUT':
        post_data = JSONParser().parser(request)
        post_data_serialized = PostSerializer(post, data=post_data)
        
        if post_data_serialized.is_valid():
            post_data_serialized.save()
            return JsonResponse(post_data_serialized.data)
        
        return JsonResponse(post_data_serialized.errors, status=400)
    
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse(status=204)
