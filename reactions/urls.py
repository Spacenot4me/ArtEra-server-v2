from django.urls import path

from reactions.views import *

app_name = 'reactions'
urlpatterns = [
    path('likes/', AllLikes.as_view()),
    path('commnets/', AllComments.as_view()),
    path('likes/<int:pk>', LikesView.as_view()),
    path('commnets/<int:pk>', CommentsView.as_view()),
    path('reactions/count/<int:post_id>', get_reactions_count, name='get_likes_by_post'),

]