from django.urls import path, include
from Classroom import views

urlpatterns = [
    path('create_classroom/', views.create_classroom, name="create_classroom"),
    path('add_student/', views.add_student, name="add_student"),

]
