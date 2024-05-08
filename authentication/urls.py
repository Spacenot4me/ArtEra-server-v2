from django.urls import path


from .views import *
app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/<int:pk>', GetUserAPI.as_view()),
    path('users/kant', GetAllUsersAPI.as_view())
]

