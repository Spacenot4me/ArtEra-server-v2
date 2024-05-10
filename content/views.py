from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from rest_framework import status, filters
from rest_framework.response import Response
from django.http import JsonResponse
import requests
import base64
from django.http import HttpResponse
from PIL import Image
import io
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

class GenImageCollector(generics.ListCreateAPIView):
    queryset = ImageCollector.objects.all()
    serializer_class = ImageCollectorSerializer



def send_and_receive_json(request):
    url = 'http://127.0.0.1:7860/sdapi/v1/txt2img'  # Замените на ваш URL
    data = {
        "prompt": "beautiful dog",
        "negative_prompt": "",
        "styles": [""],
        "seed": -1,
        "steps": 10,
        "width": 512,
        "height": 512
    }
    response = requests.post(url, json=data)
    response_data = response.json()

    # Предполагается, что 'images' содержит изображение в формате base64
    image_base64 = response_data.get('images')
    return JsonResponse(image_base64[0], safe=False)



