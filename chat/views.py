from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatSerializer
from .models import Chat



class GetChat(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializer

    def get(self, request):
        chat, created = Chat.objects.get_or_create(initiator__id=request.user.pk)
        serializer = self.serializer_class(instance=chat)
        return Response({"message": "Chat gotten", "data": serializer.data}, status=status.HTTP_200_OK)
