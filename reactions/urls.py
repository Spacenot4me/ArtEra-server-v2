from django.urls import path

from reactions.views import *

app_name = 'reactions'
urlpatterns = [
    path('likes/', AllLikes.as_view()),
    path('commnets/', AllComments.as_view()),
    path('likes/<int:pk>', LikesView.as_view()),
    path('commnets/<int:pk>', CommentsView.as_view()),
    path('reactions/count/', get_reactions_count, name='get_likes_by_post_and_is_user_liked_post'),
    path('reactions/likedposts/<int:owner_id>', get_liked_posts, name='get_liked_posts_of_user'),
    path('reactions/safelike/', safe_create_delete_like, name='create_or_delete_like')
]