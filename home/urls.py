from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('' , views.index, name ='home'),
    path('update/<str:pk>/', views.updateTask, name = "update"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete"),
    path('search' , views.search, name = 'search'),
    path('test' , views.test, name = 'test')


    
]
