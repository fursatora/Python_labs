"""
URL configuration for Hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info, name='info'),


    path('guests/new/', views.guest_new, name='guest_new'),
    path('guests/<int:pk>/', views.student_detail, name='guest_detail'),
    path('students/<int:pk>/edit/', views.student_edit, name='guest_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='guest_delete'),

    path('rooms/new/', views.room_new, name='room_new'),
    path('workers/<int:pk>/', views.room_detail, name='room_detail'),
    path('workers/<int:pk>/edit/', views.room_edit, name='room_edit'),
    path('workers/<int:pk>/delete/', views.room_delete, name='room_delete'),
]
