from django.urls import path
from . import views
from .views import(userDeleteByName)

app_name = 'user_api_app'

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('user-list/', views.userList, name='user-list'),
    path('user-detail/', views.userDetailByName, name='user-detail-by-name'),
    path('user-detail/<str:pk>/', views.userDetailById, name='user-detail-by-id'),
    path('user-create/', views.userCreate, name='user-create'),
    path('user-update/', views.userUpdateByName, name='user-update-by-name'),
    path('user-update/<str:pk>/', views.userUpdateById, name='user-update-by-id'),
    path('user-delete-by-name/', userDeleteByName, name='user-delete-by-name'),
    path('user-delete/<str:pk>/', views.userDeleteById, name='user-delete-by-id'),
]

  