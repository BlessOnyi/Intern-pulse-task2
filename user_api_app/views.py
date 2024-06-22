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




# Viewing or retrieving individual Details

@api_view(['GET'])
def userDetailByName(request):
    username = request.query_params.get('username', None)
    if username is None:
        return Response({'error': 'Username is required as a query parameter'}, status=status.HTTP_400_BAD_REQUEST)
    user = get_object_or_404(User, username=username)
    serializer = MyUserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def userDetailById(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = MyUserSerializer(user)
    return Response(serializer.data)





# Updating the User
@api_view(['PUT'])
def userUpdateByName(request):
    old_name = request.query_params.get('old_name', None)
    if old_name is None:
        return Response({'error': 'Old name is required as a query parameter'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=old_name)
    serializer = MyUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def userUpdateById(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = MyUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# Create User
@api_view(['POST'])
def userCreate(request):
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = request.data.get('password')

    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not password:
        return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)

    
    user = User(username=username, first_name=first_name, last_name=last_name, email=email)
    user.set_password(password)  
    user.save()

    
    serializer = MyUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)




# Deleting User either with Username in the datebase or ID
@api_view(['DELETE'])
def userDeleteByName(request):
    username = request.query_params.get('username', None)
    if username is None:
        return Response({'error': 'Username is required as a query parameter'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)
    user.delete()
    return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['DELETE'])
def userDeleteById(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)






