from django.db import models


# Create your models here.
class Comment(models.Model):
    #id
    owner_id = models.BigIntegerField()  # TODO id пользователя
    post_id = models.BigIntegerField()
    text = models.TextField()  # Text of the comment
    published_at = models.DateTimeField(auto_now=True)  # Date when published

    def __str__(self):
        return self.owner_id


class Like(models.Model):
    #id
    owner_id = models.BigIntegerField()  # Owner of the like
    post_id = models.BigIntegerField()  # Post which liked

    def __str__(self):
        return self.owner_id
