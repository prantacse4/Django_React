from django.urls import path, include
from Accounts import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', obtain_auth_token, name="login"),
    path('user/', views.current_user, name="user"),
    path('update_user/', views.update_user, name="update_user"),
    path('change_password/', views.change_password, name="change_password"),
    path('verify/', views.verify, name="verify"),
    path('destroy/', views.destroy, name="destroy"),
    path('update_profile_pic/', views.update_profile_pic, name="update_profile_pic"),
    path('i_am_a_student/', views.i_am_a_student, name="i_am_a_student"),
    path('i_am_a_teacher/', views.i_am_a_teacher, name="i_am_a_teacher"),
]
