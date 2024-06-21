from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyUserSerializer
from .models import User
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/user-list/',
        'Detail View': '/user-detail/<str:pk>/',
        'Create': '/user-create/',
        'Update': '/user-update/<str:pk>/',
        'Delete': '/user-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = MyUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = MyUserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def userUpdate(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    old_name = request.query_params.get('old_name')
    if old_name:
        if old_name != user.username:
            return Response({'error': 'Old name does not match the current user name'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = MyUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def userCreate(request):
    # Extract the user's name from the request data
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = request.data.get('password')

    # Create the user
    user = User(username=username, first_name=first_name, last_name=last_name, email=email)
    user.set_password(password)  # Ensure you set the password correctly
    user.save()

    # Serialize the user and return the response
    serializer = MyUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def userDelete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response("User deleted successfully.")
