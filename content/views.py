from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
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
    filterset_fields = ['owner']
    search_fields = ['title']

    def get_queryset(self):
        sort_by = self.request.query_params.get('sort', '-id')
        return Post.objects.all().order_by(sort_by)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class GenImageCollector(generics.ListCreateAPIView):
    queryset = ImageCollector.objects.all()
    serializer_class = ImageCollectorSerializer

    def create(self, request, *args, **kwargs):
        # Получаем prompt из запроса
        prompt = request.data.get("prompt")

        # Отправляем prompt в модель DALL-E
        client = OpenAI()
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Получаем URL сгенерированной картинки
        image_url = response.data[0].url

        # Создаем объект ImageCollector и сохраняем результат
        owner = request.user.id  # Предполагается, что у вас есть аутентификация пользователей
        image_collector = ImageCollector.objects.create(
            prompt=prompt,
            owner=owner,
            picture=image_url,
        )

        # Возвращаем успешный ответ
        return Response(
            {"message": "Изображение успешно сохранено", "image_url": image_url},
            status=status.HTTP_201_CREATED,
        )