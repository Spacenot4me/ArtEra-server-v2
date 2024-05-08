from django.urls import path

from reactions.views import *

app_name = 'reactions'
urlpatterns = [
    path('likes/', AllLikes.as_view()),
    path('commnets/', AllComments.as_view()),
    path('likes/<int:pk>', LikesView.as_view()),
    path('commnets/<int:pk>', CommentsView.as_view()),
    path('reactions/count/<int:post_id>', get_reactions_count, name='get_likes_by_post'),
    path('reactions/check/like/<int:post_id>/<int:owner_id>', is_liked, name='is_post_liked_by_user'),
    path('reactions/likedposts/<int:owner_id>', get_liked_posts, name='get_liked_posts_of_user')
]