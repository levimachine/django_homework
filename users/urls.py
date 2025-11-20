from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, UserUpdateView, reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_create'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('verify/<int:pk>', UserUpdateView.as_view(), name='user_verify'),
    path('reset_password', reset_password, name='reset_password')
]
