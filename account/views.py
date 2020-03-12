from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from account.serializers import AccountSerializer, AccountStatusSerializer
from account.models import Account
from rest_framework import status as resp_status


@api_view(['GET'])
def ping(request):
    return Response({'status': 200, 'result': True}, status=resp_status.HTTP_200_OK)


@api_view(['GET'])
def add(request):
    data = AccountSerializer(data=request.data)
    if not data.is_valid():
        return Response({'status': 400, 'result': False}, status=resp_status.HTTP_404_NOT_FOUND)
    uuid = data.validated_data['uuid']
    value = data.validated_data['value']
    try:
        model = Account.objects.get(pk=uuid)
    except ObjectDoesNotExist:
        return Response({'status': 400, 'result': False}, status=resp_status.HTTP_404_NOT_FOUND)
    if not model.status:
        return Response({'status': 405,
                         'result': False,
                         'addition': {
                             'uuid': model.uuid,
                             'name': model.name,
                             'balance': model.balance,
                             'status': model.status
                         },
                         'description': {
                             'status': 'Счет закрыт'
                         }},
                        status=resp_status.HTTP_405_METHOD_NOT_ALLOWED)
    model.balance += value
    model.save()
    return Response({'status': 200,
                     'result': True,
                     'addition': {
                         'uuid': model.uuid,
                         'name': model.name,
                         'balance': model.balance,
                         'status': model.status
                     },
                     'description': {
                         'status': 'Счет пополнен'
                     }},
                    status=resp_status.HTTP_200_OK)


@api_view(['GET'])
def substract(request):
    data = AccountSerializer(data=request.data)
    if not data.is_valid():
        return Response({'status': 400, 'result': False}, status=resp_status.HTTP_404_NOT_FOUND)
    uuid = data.validated_data['uuid']
    value = data.validated_data['value']
    try:
        model = Account.objects.get(pk=uuid)
    except ObjectDoesNotExist:
        return Response({'status': 400, 'result': False}, status=resp_status.HTTP_404_NOT_FOUND)
    if not model.status:
        return Response({'status': 405,
                         'result': False,
                         'addition': {
                             'uuid': model.uuid,
                             'name': model.name,
                             'balance': model.balance,
                             'status': model.status
                         },
                         'description': {
                             'status': 'Счет закрыт'
                         }},
                        status=resp_status.HTTP_405_METHOD_NOT_ALLOWED)
    result = model.balance - model.hold - value
    is_possible = True if result >= 0 else False
    if not is_possible:
        return Response({'status': 405,
                         'result': False,
                         'addition': {
                             'uuid': model.uuid,
                             'name': model.name,
                             'balance': model.balance,
                             'status': model.status
                         },
                         'description': {
                             'status': 'Недостаточно средств'
                         }},
                        status=resp_status.HTTP_405_METHOD_NOT_ALLOWED)
    model.balance = result
    model.save()
    return Response({'status': 200,
                     'result': True,
                     'addition': {
                         'uuid': model.uuid,
                         'name': model.name,
                         'balance': model.balance,
                         'status': model.status
                     },
                     'description': {
                         'status': 'Списание произведено'
                     }},
                    status=resp_status.HTTP_200_OK)


@api_view(['GET'])
def status(request):
    data = AccountStatusSerializer(data=request.data)
    if not data.is_valid():
        return Response({'status': 400, 'result': False}, status=resp_status.HTTP_404_NOT_FOUND)
    uuid = data.validated_data['uuid']
    try:
        model = Account.objects.get(pk=uuid)
    except ObjectDoesNotExist:
        return Response({'status': 400, 'result': False}, status=resp_status.HTTP_404_NOT_FOUND)
    if not model.status:
        return Response({'status': 405,
                         'result': False,
                         'addition': {
                             'uuid': model.uuid,
                             'name': model.name,
                             'balance': model.balance,
                             'status': model.status
                         },
                         'description': {
                             'status': 'Счет закрыт'
                         }},
                        status=resp_status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response({'status': 200,
                     'result': True,
                     'addition': {
                         'uuid': model.uuid,
                         'name': model.name,
                         'balance': model.balance,
                         'status': model.status
                     },
                     'description': {
                         'status': 'Счет открыт'
                     }},
                    status=resp_status.HTTP_200_OK)
