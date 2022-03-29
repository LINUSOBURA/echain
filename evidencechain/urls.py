"""echain URL Configuration

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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing, name ='landing'),
    path('login', views.login, name ='login'),
    path('logout', views.logout, name ='logout'),
    path('home', views.home, name='home'),
    path('create_case', views.create_case, name ='create_case'),
    path('cases', views.cases, name ='cases'),
    path('evidence', views.evidence, name='evidence' ),
    path('add_evidence', views.add_evidence, name ='add_evidence'),
    path('case/<str:pk>', views.case, name ='case'),
    path('s_evidence/<str:pk>', views.s_evidence, name='s_evidence'),
    path('closed', views.closed, name ='closed'),
    path('integrity', views.check_integrity, name='integrity')
]
