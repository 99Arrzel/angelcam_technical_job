from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
import json
from app.settings import API_ENDPOINT


# https://developers.angelcam.com/#tag/shared-camera-recording
@api_view(['GET'])
def shared_cameras(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response({'error': 'Missing Authorization header'}, status=401)
    if not token:
        return Response({'error': 'Missing token'}, status=401)
    response = requests.get(f'{API_ENDPOINT}/shared-cameras',
                            headers={'Authorization': f'PersonalAccessToken {token}',
                                     'Accept': 'application/json',
                                     })
    if response.status_code == 200:
        return Response(response.json())
    return Response({'error': 'Invalid token'}, status=401)
