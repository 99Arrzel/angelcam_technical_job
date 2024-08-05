from django.urls import path
from angelcam.endpoints.landing import getData
from angelcam.endpoints.auth import auth_me
from django.conf import settings

urlpatterns = [
  path('', getData),
  path('auth', auth_me), 
]