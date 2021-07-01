from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from Accounts.models import *


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyClassroom
        fields = ['title','teacher']

class AddClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudents
        fields = ['classroom','student']
