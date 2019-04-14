import re, json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from Tips.models import *
# from . import serializers
from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create a new Location
def create_location(name):
    temp = Location.objects.filter(name=name)
    if (temp.count() > 0):
        return temp

    l = Location()
    l.name = name
    l.lat = ""
    l.lon = ""
    l.save()
    return l

# Creates a new post
@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_post(request):
    # Get the user associated with the token
    token = request.META['HTTP_AUTHORIZATION'][6:]
    user = Token.objects.get(key=token).user

    # Get the JSON sent to the server
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    if 'data' in body:
        body = json.loads(body['data'])

    # Create the new post
    post = Post()
    post.author = user.profile
    post.title = body['title']
    post.content = body['contents']
    post.is_question = body['is_question']
    
    # If location was submitted, create it
    if (len(body['location']) > 0):
        post.location = create_location(body['location'])

    # Save the new post
    post.save()

    return Response({'success': 'Post successfully created.'}, status=HTTP_200_OK)
