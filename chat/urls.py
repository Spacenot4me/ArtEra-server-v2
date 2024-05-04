from django.urls import path
from .views import GetChat
app_name = 'chat'
urlpatterns = [
    path("all", GetChat.as_view(), name="get-chats"),
]
