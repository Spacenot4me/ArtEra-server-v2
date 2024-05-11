from django.urls import path
from .views import *

app_name = 'content'
urlpatterns = [
    path('posts/', PostListCreate.as_view()),
    path('posts/<int:pk>', PostRetrieveUpdateDestroy.as_view()),
    path('genImages/', GenImageCollector.as_view()),
    path('generate_image/', send_and_receive_json, name="generate image in base64"),
    path('generate_image/getstatus/', get_status_of_generation, name="get status of generation"),
]
