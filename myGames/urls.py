"""
URL configuration for myGames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import include #importing the include function to include the URLs from the guesser app

from Core import views #importing the views from the Core app to use in the URL patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #this is the home page of the website. It will display a welcome message to the user.   
    path('guesser/', include('guesser.urls')), #this is the URL for the guesser game. It will include the URLs from the guesser app.
]
