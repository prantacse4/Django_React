from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_member = models.BooleanField(default=True)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)





class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tid = models.CharField(max_length=250, blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    university = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.user.username








class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.CharField(max_length=250, blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    session = models.CharField(max_length=250, blank=True, null=True)
    batch = models.CharField(max_length=250, blank=True, null=True)
    semester = models.CharField(max_length=250, blank=True, null=True)
    university = models.CharField(max_length=250, blank=True, null=True)


    def __str__(self):
        return self.user.username






class UserProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploaded_image/user", blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_dp(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfileImage.objects.create(user=instance)



class MyClassroom(models.Model):
    title = models.CharField(max_length=250)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ClassStudents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(MyClassroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.classroom.title