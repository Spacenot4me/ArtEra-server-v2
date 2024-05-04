from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics,status, filters
from reactions.models import Like, Comment
from reactions.serializers import LikesSerializer, CommentsSerializer


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