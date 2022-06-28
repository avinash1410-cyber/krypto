from django.urls import path
from .views import AlertAPIView,trigerred,DeleteAPIView,LogoutView,CreateAlert,Register,filter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView





urlpatterns = [
    path('create/',CreateAlert.as_view()),
    path('delete/',DeleteAPIView),
    path('', AlertAPIView.as_view()),
    path('<int:pk>/',AlertAPIView.as_view()),
    path('trigerred/',trigerred),
    path('logout/',LogoutView),
    path('register/',Register.as_view(),name="register"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('filter/', filter, name='token_verify'),
]