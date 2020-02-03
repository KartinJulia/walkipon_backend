import json
import requests
import urllib.request
from copy import deepcopy
from django.conf import settings
#from django.shortcuts import render
from django.contrib import auth
#from django.contrib.auth import authenticate
#from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
#from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from graffiti_backend.commons import HTTPMethod, GraffitiBackendMethod
from user_authentication.commons import UserType, UserSearchIdentifier
from user_authentication.logics.user_factory import UserFactory


@api_view(['POST', ])
#@permission_classes((IsAuthenticated, ))
@permission_classes((AllowAny, ))
#@permission_classes((AllowAny, IsAuthenticated,))
@csrf_exempt
def user_view_handler(request):
    if 'method' not in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if 'user_type' not in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == HTTPMethod.POST.value:
    #if request.method == 'POST':
        data_dictionary = deepcopy(request.data)
        if request.data['method'] == GraffitiBackendMethod.CREATE.value:
            request.data.pop('user_type')
            request.data.pop('method')
            if request.data['profile_image'] != None:
                request.data.pop('profile_image')
            auth0_token_request = requests.post("https://" + getattr(settings, "AUTH0_DOMAIN", None) + "/dbconnections/signup", data=request.data)
            if (auth0_token_request.status_code == status.HTTP_201_CREATED) or (auth0_token_request.status_code == status.HTTP_200_OK):
                UserFactory.create_user(data_dictionary)
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=auth0_token_request.status_code)
        elif request.data['method'] == GraffitiBackendMethod.UPDATE.value:
            auth_user = request.user
            #auth_user = json.loads(smart_text(request.body));
            auth_user_id = auth_user.user_id
            if auth_user_id is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            logic_user = UserFactory.get_logic_user(UserSearchIdentifier.USER_ID, auth_user_id)
            UserFactory.update_user(data_dictionary, logic_user)
            UserFactory.write_database_handler(UserSearchIdentifier.USER_ID, logic_user)
            return Response(status=status.HTTP_200_OK)
        elif request.data['method'] == GraffitiBackendMethod.READ.value:
            auth_user = request.user
            auth_user_id = auth_user.user_id
            if auth_user_id is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            logic_user = UserFactory.get_logic_user(UserSearchIdentifier.USER_ID, auth_user_id)
            user_data_json = UserFactory.get_user_json(logic_user)
            return Response(user_data_json, status=status.HTTP_200_OK)
        #TODO: delete user
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', ])
@permission_classes((AllowAny, ))
@csrf_exempt
def login_view_handler(request):
    if request.method == HTTPMethod.POST.value:
        if 'username' not in request.data or 'password' not in request.data:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        auth0_token_request = requests.post("https://" + getattr(settings, "AUTH0_DOMAIN", None) + "/oauth/token", data=request.data)
        if auth0_token_request.status_code != status.HTTP_200_OK:
            return Response(status=auth0_token_request.status_code)
        user = auth.authenticate(email=request.data['email'], password=request.data['password'])
        if user is not None and user.is_active:
            auth.login(request, user)
            logic_user = UserFactory.get_logic_user(UserSearchIdentifier.USER_EMAIL.value, user)
            user_data_json = UserFactory.get_user_json(logic_user)
            return Response({"user_data":user_data_json, "auth0_jwt":json.loads(auth0_token_request.text)}, status=auth0_token_request.status_code)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', ])
#@permission_classes((AllowAny, ))
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def logout_view_handler(request):
    if request.method == HTTPMethod.POST.value:
        try:
            auth.logout(request)
            requests.get("https://" + getattr(settings, "AUTH0_DOMAIN", None) + "/oauth/revoke", json=request.data)
        except KeyError:
            pass
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
