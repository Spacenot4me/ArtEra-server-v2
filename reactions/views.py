from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, status, filters
from reactions.models import Like, Comment
from reactions.serializers import LikesSerializer, CommentsSerializer
import requests

# Create your views here.


class AllLikes(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikesSerializer


class AllComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['post_id']


class CommentsView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = 'pk'


class LikesView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikesSerializer
    lookup_field = 'pk'


def get_reactions_count(request, post_id):
    """
    View-функция для подсчета лайков по post_id.

    Args:
        request: HTTP-запрос.
        post_id: ID поста, по которому нужно подсчитать лайки.

    Returns:
        JsonResponse с количеством лайков.
    """

    comment_count = Comment.objects.filter(post_id=post_id).count()
    like_count = Like.objects.filter(post_id=post_id).count()
    data = {
        "comment_count": comment_count,
        "like_count": like_count
    }
    return JsonResponse(data)


def is_liked(request, owner_id, post_id):
    if Like.objects.filter(owner_id=owner_id, post_id=post_id).exists():
        return JsonResponse({"is_liked": True})
    else:
        return JsonResponse({"is_liked": False})

"""
def get_liked_posts(request, owner_id):
    liked_posts = Like.objects.filter(owner_id=owner_id).values_list('post_id', flat=True)
    return JsonResponse({"liked_posts": list(liked_posts)})
"""
def get_liked_posts(request, owner_id):
    liked_posts_ids = Like.objects.filter(owner_id=owner_id).values_list('post_id', flat=True)
    liked_posts = []
    for post_id in liked_posts_ids:
        response = requests.get(f'http://localhost:8000/api/posts/{post_id}')
        if response.status_code == 200:
            liked_posts.append(response.json())
    return JsonResponse({"liked_posts": liked_posts})
