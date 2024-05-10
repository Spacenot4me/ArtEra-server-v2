from django.db import models
from datetime import datetime, timedelta
from openai import OpenAI
from rest_framework import status
from rest_framework.response import Response


# Create your models here.

class Post(models.Model):
    # id
    title = models.CharField(max_length=100)  # name of post
    description = models.CharField(max_length=1000)  # TODO поменять лимит
    owner = models.BigIntegerField()  # TODO id пользователя
    picture = models.ImageField(upload_to='images')  # TODO сделать статику с хранением картинок
    published_at = models.DateTimeField(auto_now=True)  # Date when published

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.title


class ImageCollector(models.Model):
    # id
    prompt = models.TextField()
    owner = models.BigIntegerField()
    picture = models.ImageField(upload_to='generetared_images')
    published_at = models.DateTimeField(auto_now=True)  # Date when published

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.owner


