import json
from copy import deepcopy
from django.contrib.gis.measure import Distance, D
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from graffiti_backend.commons import HTTPMethod, GraffitiBackendMethod, GraffitiOption
from message.commons import MessageType, MessageSearchIdentifier
from message.logics.message_DAO_factory import MessageDAOFactory
from user_authentication.decorators import requires_auth
from user_authentication.logics.user_factory import UserFactory
from user_authentication.commons import UserType, UserSearchIdentifier
from datetime import datetime

from message.serializers.criteria_serializers import CriteriaCreateSerializer

@api_view(['POST', 'GET', ])
@permission_classes((IsAuthenticated, ))
#@permission_classes((AllowAny, ))
@csrf_exempt
@requires_auth
def commercial_user_coupon_message_view_handler(request, user_id=None, message_id=None):
    auth_user = request.user
    auth_user_id = auth_user.id
    
    #data_dictionary = deepcopy(request.data.dict())
    if user_id == None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if int(user_id) != auth_user_id or auth_user_id == None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    user = UserFactory.get_logic_user(UserSearchIdentifier.USER_ID.value, auth_user_id)
    if user.get_user_type() != UserType.COMMERCIAL_USER.value:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    #data_dictionary['user_id'] = auth_user_id

    if request.method == HTTPMethod.POST.value:
        data_dictionary = deepcopy(request.data.dict())
        data_dictionary['user_id'] = auth_user_id
        if 'method' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        #data_dictionary = deepcopy(request.data.dict())
        if request.data['method'] == GraffitiBackendMethod.CREATE.value:
            if 'longitude' not in request.data or 'latitude' not in request.data:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            data_dictionary['location'] = '['+request.data['longitude']+', '+request.data['latitude']+']'
            if 'message_type' not in request.data:
                data_dictionary['message_type'] = MessageType.COUPON_MESSAGE.value
            user.create_coupon_message(data_dictionary)
            return Response(status=status.HTTP_201_CREATED)
        elif request.data['method'] == GraffitiBackendMethod.UPDATE.value:
            if 'option' not in request.data or message_id == None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if request.data['option'] == GraffitiOption.MODIFY.value:
                try:
                    user.update_coupon_message(message_id, data_dictionary)
                except ValueError:
                    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == HTTPMethod.GET.value:
        '''
        TODO: listing commerical user posted coupon info. User can select it for updating and deleting.
        '''
        data_dictionary = deepcopy(request.data)
        data_dictionary['user_id'] = auth_user_id
        if request.GET['method'] != GraffitiBackendMethod.READ.value:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if 'offset' not in request.GET or 'limit' not in request.GET:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if request.GET['option'] == GraffitiOption.OVERVIEW.value:
            if 'message_type' not in request.GET:
                message_json = user.get_message_overview_json(request.GET['offset'], request.GET['limit'], MessageType.COUPON_MESSAGE.value)
            else:
                message_json = user.get_message_overview_json(request.GET['offset'], request.GET['limit'], request.GET['message_type'])
            #print(message_json)
            return Response(message_json, status=status.HTTP_200_OK)
        elif request.GET['option'] == GraffitiOption.DETAIL.value:
            if 'message_type' not in request.GET:
                message_json = user.get_message_detail_json(request.GET['offset'], request.GET['limit'], MessageType.COUPON_MESSAGE.value)
            else:
                message_json = user.get_message_detail_json(request.GET['offset'], request.GET['limit'], request.GET['message_type'])
            return Response(message_json, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
@requires_auth
def nearby_coupon_messages_view_handler(request):
    if request.method == HTTPMethod.GET:
        auth_user = request.user
        auth_user_id = auth_user.id
        data_dictionary = deepcopy(request.data)
        data_dictionary['user_id'] = auth_user_id
        if auth_user_id is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if 'longitude' not in request.GET or 'latitude' not in request.GET or 'radius' not in request.GET:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data_dictionary['location'] = '['+request.GET['longitude']+', '+request.GET['latitude']+']'
        data_dictionary['radius'] = request.GET['radius']
        if 'offset' in request.GET and 'limit' in request.GET:
            data_dictionary['offset'] = request.GET['offset']
            data_dictionary['limit'] = request.GET['limit']
        elif 'offset' not in request.GET and 'limit' not in request.GET:
            data_dictionary['offset'] = None
            data_dictionary['limit'] = None
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        logic_messages = MessageFactory.get_logic_messages(MessageSearchIdentifier.LOCATION, data_dictionary, MessageType.COUPON_MESSAGE)
        if 'option' not in request.GET:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if request.GET['option'] == GraffitiOption.OVERVIEW:
            coupon_messages_overview_json = MessageFactory.get_messages_overview_json(logic_messages, MessageType.COUPON_MESSAGE)
            return Response(coupon_messages_overview_json, status=status.HTTP_200_OK)
        elif request.GET['option'] == GraffitiOption.DETAIL:
            #for logic_message in logic_messages:
            #    MessageFactory.increase_message_read_times(logic_message)
            #    MessageFactory.write_database_handler(logic_message)
            coupon_messages_detail_json = MessageFactory.get_messages_detail_json(logic_messages, MessageType.COUPON_MESSAGE)
            return Response(coupon_messages_detail_json, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

