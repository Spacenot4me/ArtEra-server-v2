from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer
from rest_framework import status, filters
from rest_framework.response import Response


# Create your views here.
class PostListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'count': self.page.paginator.count,
            'results': data
        })


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostListPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['owner']  # добавьте это\
    search_fields = ['title']

    def get_queryset(self):
        # get the sort parameter value from request
        sort_by = self.request.query_params.get('sort', '-id')
        return Post.objects.all().order_by(sort_by)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
