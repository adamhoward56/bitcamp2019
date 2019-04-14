import re, json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
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

# USER LOGIN
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    # Decode the request body
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    if 'data' in body:
        body = json.loads(body['data'])

    # Get the proper values
    username = body['username']
    password = body['password']
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    
    # Handle if they used an email address
    if "@" in username:
        try:
            usr = User.objects.get(email=username)
            username = usr.username
        except User.DoesNotExist:
            return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


# USER REGISTRATION
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    # Parse the JSON to get fields
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    if 'data' in body:
        body = json.loads(body['data'])

    username = body['username']
    email = body['email']
    password = body['password']
    confirm_password = body['confirm_password']
    error = []

    # Make sure all fields are provided
    if username is None or email is None or password is None or confirm_password is None:
        return Response({'error': 'All fields must be filled out.'}, status=HTTP_400_BAD_REQUEST)

    # Check parameter lengths
    if len(username) < 3 or len(username) > 30:
        error.append("Username must be between 3 and 30 characters.")
    if len(password) < 8 or len(password) > 50 or len(confirm_password) < 8 or len(confirm_password) > 50:
        error.append("Password must be between 8 and 50 characters.")
    if len(email) > 100:
        error.append("Email address must be 100 characters or less.")

    # Confirm that password was entered correctly twice
    if not password == confirm_password:
        error.append("Passwords do not match.")

    # Check if email already exists
    if (User.objects.filter(username=username).count() != 0):
        error.append("Username is already in use.")

    # Check if email already exists
    if (User.objects.filter(email=email).count() != 0):
        error.append("Email address is already in use.")

    # Username has invalid characters
    if not re.match(r"^[A-Za-z0-9_-]*$", username):
        error.append("Username may only contain alphanumeric characters, underscores, and dashes.")

    # Password has invalid characters
    if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        error.append("Only alphanumeric characters and @#$%^&+= may be used for passwords.")
    
    # Check for valid email address
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        error.append("A valid email address must be provided.")

    # Return an error if the stuff provided is bad
    if (len(error) > 0):
        return Response({'error': error}, status=HTTP_400_BAD_REQUEST)

    # Create the new user
    new_user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'success': 'User successfully created.'}, status=HTTP_200_OK)
    

def failure( request ):
    return HttpResponse("Nothing here.")

# API TESTS
class TestAuth(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Successfully GET request with authenticated token!'}
        return Response(content)

class TestNoAuth(APIView):
    def get(self, request):
        content = {'message': 'Successful GET request without authentication!'}
        return Response(content)