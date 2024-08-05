from django.urls import path
from angelcam.endpoints.landing import getData
from angelcam.endpoints.auth import auth_me
from angelcam.endpoints.my_cameras import shared_cameras
from django.conf import settings

urlpatterns = [
  path('', getData),
  path('auth', auth_me), 
  path('shared-cameras', shared_cameras),
]