from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


from app.settings import API_ENDPOINT

@api_view(['GET'])
def getData(request):
  return Response('OK')
