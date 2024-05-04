from rest_framework import serializers

from .models import Comment, Like


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['owner_id', 'post_id', 'text', 'published_at']


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['owner_id', 'post_id']
