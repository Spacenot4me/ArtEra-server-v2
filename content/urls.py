from django.urls import path
from .views import *

app_name = 'content'
urlpatterns = [
    path('posts/', PostListCreate.as_view()),
    path('posts/<int:pk>', PostRetrieveUpdateDestroy.as_view()),
]
