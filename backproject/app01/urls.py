"""backproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
import app01.views as views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

app_name='son'
router=routers.DefaultRouter()
# router.register('configuser',views.UserView,basename='configuser')
router.register('customuser',views.CustomUserView,basename='customuser')
router.register('gptuser',views.GptUserView,basename='gptuser')
router.register('gptformuser',views.GptFormUserView,basename='gptformuser')
router.register('upload',views.UploadView,basename='upload')
router.register('uploadpdf',views.UploadPdfView,basename='uploadpdf')
router.register('uploadjson',views.UploadJsonView,basename='uploadjson')

urlpatterns = [
    path('son/',views.test,name='test'),
    path('getchat/',views.chat,name='getchat'),
    path('getclass/',views.gtc,name='getclass'),
    path('toemail/',views.toemail,name='toemail'),
    path('check/',views.checkUE,name='checkUE'),
    path('generate/',views.generate,name='GeneratorExit'),
    path('register/',views.register,name='register')
]
urlpatterns+=router.urls