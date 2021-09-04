from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
path('login/', obtain_auth_token, name='api_token_auth'),
path('logout/',views.logout),
path('signUp/',views.signUp) ,
path('addToken/',views.sendToken),
path('sendMessage',views.sendMessage)
]
