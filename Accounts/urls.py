from django.urls import path, include
from Accounts import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', obtain_auth_token, name="login"),
    path('user/', views.current_user, name="user"),
    path('update_user/', views.update_user, name="update_user"),
    path('change_password/', views.change_password, name="change_password"),
]