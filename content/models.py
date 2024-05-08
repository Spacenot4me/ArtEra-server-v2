from django.db import models
from datetime import datetime, timedelta


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
