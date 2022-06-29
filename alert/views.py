from multiprocessing.managers import DictProxy
from django.http import HttpResponse
from requests import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from alert import serializers
from alert.serializers import AlertSerializer,UserSerializer
from .models import Alert,User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
import math

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework.pagination import PageNumberPagination
from .pagination import PaginationHandlerMixin



# Create your views here.
import requests
import json
# https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false


#print(response_API.status_code)





class BasicPagination(PageNumberPagination):
    page_size_query_param = '1'












@api_view(('GET','POST'))
def DeleteAPIView(request):
    print(request.user)
    # permission_classes=['IsAuthenticated']
    if request.method=="GET":
        return Response()
    else:
        pk=request.data
        alert=Alert.objects.get(id=pk)
        if alert is None: 
            return Response({"message":"Not Found object"})
        if alert.user!=request.user:
            print(request.user)
            return Response({"message":"You are not it owner so Cann't Be Deleted"})
        else:
            print(request.user)
            alert.delete()
        return Response({"Message":"Deleted"})



# class DeleteAPIView(APIView):
#     # permission_classes=['IsAuthenticated']
#     def get(self):
#         return Response()
#     def post(self,request):
#         pk=request.data
#         alert=Alert.objects.get(id=pk)
#         if alert is None: 
#             return Response({"message":"Not Found object"})
#         if alert.user!=request.user:
#             return Response({"message":"You are not it owner so Cann't Be Deleted"})
#         else:
#             alert.delete()
#             return Response({"Message":"Deleted"})



@api_view(('GET',))
def LogoutView(request):
    if request.method=="GET":
        print(request.user)
        logout(request)
        return  Response({'message':"Log out"})


# class LogoutView(APIView):
#     permission_classes=['IsAuthenticated']
#     def get(self,request):
#         logout(request)
#         return  Response({'message':"Log out"})



class Register(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        if username:
            print("get data")
        else:
            return Response("Try again")
        user = User.objects.create_user(username=username,password=password,email=email)
        srlzr=UserSerializer(user)
        refresh = RefreshToken.for_user(user)
        return Response({"user":srlzr.data,'refresh': str(refresh),'access': str(refresh.access_token),})
    def get(self, request):
        dict={
        "username":"",
        "password":"",
        "email":""
             }
        return Response(dict)




def email_send(list):
  subject = 'Your dream come true'
  message = f'Hi your value has been achived'
  # email_from = settings.EMAIL_HOST_USER
  # recipient_list = list
  # send_mail( subject, message, email_from, recipient_list )
  for x in list:
    print(f"Hello {x[1]} Alert is activated for {x[3]} on target value at {x[2]}")


# @api_view(('GET','POST'))
def trigerred():
    response_API =requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    data = response_API.text
    parse_json = json.loads(data)
    dict={}
    dict=parse_json
    ansdict=[]
    userlist=[]
    for x in dict:
        cv=math.floor(x['current_price'])
        cc=x['symbol']
        print(cv)
        alerts=Alert.objects.filter(alert_value=cv,status="created",coin=cc)
        for a in alerts:
            a.status="trigerred"
            a.save()
        srlzr=AlertSerializer(data=alerts,many=True)
        srlzr.is_valid()
        if len(srlzr.data)>0:
            ansdict.append(srlzr.data)
    for x in ansdict:
        for y in x:
            user=User.objects.get(id=y['user'])
            userlist.append([user.email,user.username,y['alert_value'],y['coin']])
    print(userlist)
    email_send(userlist)
    return Response(userlist)



@api_view(('GET','POST'))
def filter(request):
    print(request.user)
    if request.method=="POST":
        q=request.data['q']
        search_alerts=Alert.objects.filter(status=q,user=request.user)
        srlzr=AlertSerializer(data=search_alerts,many=True)
        srlzr.is_valid()
        return Response(srlzr.data)
    else:
        print(request.user)
        return Response({"q":""})





class AlertAPIView(APIView,PaginationHandlerMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = BasicPagination
    # @method_decorator(cache_page(3*1))
    def get(self, request, pk=None):
        print(request.user)
        if pk:
            alert=Alert.objects.get(id=pk)    
            if alert.user!=request.user:
                print("Diffrent User")
                return Response({"message":"No record Found"})
            else:
                print("Found")
                data={
                    'user':alert.user,
                    'id':alert.id,
                    'alert_value':alert.alert_value,
                    'status':alert.status
                }
                # print(alert.id)
                # print(alert.alert_value)
                # print(alert.status)
                serializer=AlertSerializer(alert)
                return Response(serializer.data)
        else:
            alerts=Alert.objects.filter(user=request.user)
            srlzr=AlertSerializer(data=alerts,many=True)
            srlzr.is_valid()
            return Response(srlzr.data)


class CreateAlert(APIView):
    def get(self, request):
        return Response({"coin":"","value":""})
    def post(self, request):
        print(request.user)
        target_value=request.data['value']
        coin=request.data['coin']
        alert=Alert.objects.create(
            alert_value=target_value,
            status="created",
            user=request.user,
            coin=coin
        )
        return Response({"Message":"Added"})