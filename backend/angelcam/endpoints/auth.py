from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
import json
from app.settings import API_ENDPOINT


# https://developers.angelcam.com/#section/Authentication
# Just a me
@api_view(['POST'])
def auth_me(request):
    if not request.body:
        return Response({'error': 'Missing body'}, status=400)
    data = json.loads(request.body)
    token = data.get('token')
    if not token:
        return Response({'error': 'Missing token'}, status=401)
    response = requests.get(f'{API_ENDPOINT}/me',
                            headers={'Authorization': f'Bearer {token}'})
    if response.status_code == 200:
        return Response(response.json())
    return Response({'error': 'Invalid token'}, status=401)
