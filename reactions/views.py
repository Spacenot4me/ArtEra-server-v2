import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, filters

from content.models import Post
from content.serializers import PostSerializer
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


def get_reactions_count(request):
    """
    View-функция для подсчета лайков по post_id.

    Args:
        request: HTTP-запрос.
        post_id: ID поста, по которому нужно подсчитать лайки.

    Returns:
        JsonResponse с количеством лайков.
    """
    owner_id = request.GET.get('owner_id')
    post_id = request.GET.get('post_id')
    if not post_id:
        return HttpResponseBadRequest('Both owner_id and post_id must be provided')

    if owner_id == '':
        owner_id = None

    comment_count = Comment.objects.filter(post_id=post_id).count()
    like_count = Like.objects.filter(post_id=post_id).count()
    is_liked = Like.objects.filter(owner_id=owner_id, post_id=post_id).exists()

    data = {
        "comment_count": comment_count,
        "like_count": like_count,
        "is_liked": False
    }

    if owner_id:
        data["is_liked"] = is_liked

    return JsonResponse(data)


"""
def get_liked_posts(request, owner_id):
    liked_posts = Like.objects.filter(owner_id=owner_id).values_list('post_id', flat=True)
    return JsonResponse({"liked_posts": list(liked_posts)})
"""



def get_liked_posts(request, owner_id):
    liked_posts_ids = Like.objects.filter(owner_id=owner_id).values_list('post_id', flat=True)
    liked_posts = []
    for post_id in liked_posts_ids:
        try:
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post, context={'request': request})
            liked_posts.append(serializer.data)
            print(serializer.data)
        except ObjectDoesNotExist:
            pass
    return JsonResponse(liked_posts, safe=False)

@csrf_exempt
def safe_create_delete_like(request):
    data = json.loads(request.body.decode('utf-8'))
    owner_id = data.get('owner_id')
    post_id = data.get('post_id')
    if not owner_id or not post_id:
        return HttpResponseBadRequest('Both owner_id and post_id must be provided')

    try:
        like = Like.objects.get(owner_id=owner_id, post_id=post_id)
        like.delete()
        return JsonResponse({'status': 'success', 'message': 'Like successfully deleted'}, status=202)
    except Like.DoesNotExist:
        try:
            Like.objects.create(owner_id=owner_id, post_id=post_id)
            return JsonResponse({'status': 'success', 'message': 'Like successfully created'}, status=201)
        except Exception as e:
            return HttpResponseBadRequest('Bad attempt to create like: {}'.format(str(e)))
