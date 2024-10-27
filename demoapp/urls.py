from django.urls import path 
from . import views 

urlpatterns = [ 
    path('index', views.index, name='index'), 

    path('about', views.about, name='sa'), 
    
    path('drinks/<str:drink_name>/',views.drinks,name="drinks_name"),
    
    ## witch differnt between 'drinks/<str:drink_name> and 'drinks/<str:drink_name/>
    
   

    
] 