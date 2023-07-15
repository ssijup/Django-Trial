
from django.urls import path
from userapp1 import views
from .views import UserLogin
from rest_framework_simplejwt.views import (
                                        TokenObtainPairView,
                                        TokenRefreshView,
                                        )

urlpatterns = [
    path("" ,views.user ,name ='user'),

    #user function using @api_view
    path("user_registeration/" ,views.user_registeration, name='user_registeration'),
    path("user_demo/" ,views.user_demo, name='user_demo'),
    # user function using APIView class
    path("UserLogin/" ,UserLogin.as_view() ,name="UserLogin"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]