from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id',
                  'title',
                  'description',
                  'owner',
                  'picture',
                  'published_at', ]
    def get_picture(self, obj):
        request = self.context.get('request')
        picture_url = obj.picture.url
        return request.build_absolute_uri(picture_url)

class ImageCollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCollector
        fields = ['id', 'prompt', 'owner', 'picture' , 'published_at']