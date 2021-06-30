from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import User
# Create your views here.
import json
from django.core import serializers
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, UserSerializer, ChangePasswordSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .permissions import IsStudent, IsAdmin, IsTeacher, IsMember

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Registration Successful"
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user = user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)



@api_view(['GET'])
def verify(request):
    user = User.objects.filter(pk = request.user.id).count()
    data = {}
    data['authenticated'] = True
    if user == 1:
        user = User.objects.get(pk = request.user.id)
        if user.is_member == True:
            data['member'] = True

        elif user.is_superuser == True:
            data['admin'] = True

        elif user.is_student == True:
            data['student'] = True

        elif user.is_teacher == True:
            data['teacher'] = True
    else:
        data['authenticated'] = False

    # serializer = UserSerializer(user)
    return Response(data)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def update_user(request):
    serializer = UserSerializer(request.user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)



@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)
    user = request.user 
    if serializer.is_valid():
        # Check old password
        if not user.check_password(serializer.data.get("old_password")):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
        # set_password also hashes the password that the user will get
        user.set_password(serializer.data.get("new_password"))
        user.save()
        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
            'data': []
        }

        return Response(response)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)