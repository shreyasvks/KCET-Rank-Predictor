"""shubbhum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',include('users.urls')),
    path('create/accountcreated/home/',include('users.urls')),
    path('create/accountcreated/home/admin/', admin.site.urls),
    path('create/accountcreated/home/cutoff/',include('users.urls')),
    path('create/accountcreated/home/displaycutoff/',include('users.urls')),
    path('create/accountcreated/home/predcollege/',include('users.urls')),
    path('create/accountcreated/home/dispredcollege/',include('users.urls')),
    path('create/accountcreated/home/predcourse/',include('users.urls')),
    path('create/accountcreated/home/dispredcourse/',include('users.urls')),
    path('create/accountcreated/home/kct/',include('users.urls')),
    path('create/accountcreated/home/diskct/',include('users.urls')),
    path('create/accountcreated/home/rank/',include('users.urls')),
    path('create/accountcreated/home/disrank/',include('users.urls')),
    path('create/',include('users.urls')),
    path('accountcreated/',include('users.urls')),
    path('login/',include('users.urls')),
    path('loginsuccess/',include('users.urls')),
]
