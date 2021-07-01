from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import *
# Create your views here.
import json
from django.core import serializers
from rest_framework.authtoken.models import Token
from .serializers import ClassSerializer, AddClassSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from Accounts.permissions import IsStudent, IsAdmin, IsTeacher, IsMember
from PIL import Image
# Create your views here.



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsTeacher])
def create_classroom(request):
    if request.method == "POST":
        serializer = ClassSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Creating Successful"
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsTeacher])
def add_student(request):
    if request.method == "POST":
        serializer = AddClassSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Adding Student Successful"
        else:
            data = serializer.errors
        return Response(data)