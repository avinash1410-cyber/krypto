"""krypto URL Configuration

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
from django.urls import path,include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from alert.views import trigerred


# from __future__ import unicode_literals
# from django.shortcuts import render,HttpResponse
# from background_task import background
# # Create your views here.
# @background(schedule=5)
# def hello():
# 	print ("Hello World!")

# def background_view(request):
#     hello(repeat=10)
#     return HttpResponse("Hello world !")


import datetime,time

import threading


class TestThreading(object):
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            # print(datetime.datetime.now().__str__() + ' : Start task in the background')
            trigerred()
            time.sleep(self.interval)

tr = TestThreading()
time.sleep(1)
print(datetime.datetime.now().__str__() + ' : First output')
time.sleep(2)
print(datetime.datetime.now().__str__() + ' : Second output')






# from alert.views import trigerred
# def looper(request):
#     if request.method=="GET":
#         while True:
#             trigerred("GET")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('alert/', include('alert.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('',looper),
    ]
