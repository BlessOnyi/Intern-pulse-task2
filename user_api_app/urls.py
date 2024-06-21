from django.urls import path
from . import views

app_name ='user_api_app'
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('user-list/', views.userList, name="user-list"),
    path('user-detail/<str:pk>/', views.userDetail, name="user-Detail"),
    path('user-update/<str:pk>/', views.userUpdate, name="user-update"),
    path('user-create/', views.userCreate, name="user-create"),
    path('user-delete/<str:pk>/', views.userDelete, name="user-delete"),
  ]
  

  