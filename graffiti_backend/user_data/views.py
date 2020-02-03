import requests
import urllib.request
from copy import deepcopy
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
#from user_data.commons import UserDataCategory
#from user_data.logics.user_DAO_factory import UserDAOFactory
from user_authentication.decorators import requires_auth
from user_authentication.logics.user_factory import UserFactory
from user_authentication.commons import UserType, UserSearchIdentifier


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
#@permission_classes((AllowAny, ))
@csrf_exempt
@requires_auth
def user_location_view_handler(request, user_id=None):
    auth_user = request.user
    auth_user_id = auth_user.id
    data_dictionary = deepcopy(request.data)
    if user_id == None or int(user_id) != auth_user_id or auth_user_id == None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    if 'longitude' not in request.data or 'latitude' not in request.data or 'time' not in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    data_dictionary['user_id'] = auth_user_id
    data_dictionary['location'] = '['+request.data['longitude']+', '+request.data['latitude']+']'
    #UserDAOFactory.create_data(data_dictionary, UserDataCategory.LOCATION_DATA)
    user = UserFactory.get_logic_user(UserSearchIdentifier.USER_ID.value, auth_user_id)
    if user.get_user_type() != UserType.PERSONAL_USER.value:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    user.create_user_current_location(data_dictionary)
    return Response(status=status.HTTP_201_CREATED)
