from rest_framework import serializers

from .models import *


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']

class PostSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    image_details = PostImageSerializer(many=True, read_only=True, source='images')

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'owner', 'published_at', 'images', 'image_details']

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        post = super().create(validated_data)
        for image in images:
            PostImage.objects.create(post=post, image=image)
        return post

    def update(self, instance, validated_data):
        images = validated_data.pop('images', [])
        post = super().update(instance, validated_data)
        for image in images:
            PostImage.objects.create(post=post, image=image)
        return post

class ImageCollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCollector
        fields = ['id', 'prompt', 'owner', 'picture' , 'published_at']

