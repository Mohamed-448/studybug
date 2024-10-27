from django.urls import path,include
from django.http import HttpResponse
from . import views
from .views import register




urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout',views.logoutUser,name='logout'),
    path('login',views.loginPage,name="login"),
    path('', views.home, name='home'),
    path('profile/<str:pk>/',views.userProfile,name='user-profile'),
    path('room/<str:pk>/', views.room, name='room'),
    # path('room/<str:drink_name>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    
   path('update-user/', views.updateUser, name="update-user"),
     
   path('topics/', views.topicsPage, name="topics"),
    
    path('activity/', views.activityPage, name="activity"),

]


