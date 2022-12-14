from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import DepositCreateAPISerializer, AccountSerializer, WithdrawCreateAPISerializer
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

login_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'amount':openapi.Schema(type=openapi.FORMAT_FLOAT, description='float'),
        'account':openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
    },
    required=['amount', 'account']
)

class DepositCreateAPI(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    
    @swagger_auto_schema(request_body=login_schema)
    def post(self, request, *args, **kwargs):
        """
        Make deposit
        Parameters
        ---------- 
            amount, account
        """
        data = request.data
        deposit = DepositCreateAPISerializer(data=data, context={"request": request})
        deposit.is_valid(raise_exception=True)
        account = deposit.save()
        serializer = AccountSerializer(instance=account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class WithdrawCreateAPI(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    
    @swagger_auto_schema(request_body=login_schema)
    def post(self, request, *args, **kwargs):
        """
        Make withdrawal
        Parameters
        ---------- 
            amount, account
        """
        data = request.data
        withdraw = WithdrawCreateAPISerializer(data=data, context={"request": request})
        withdraw.is_valid(raise_exception=True)
        account = withdraw.save()
        breakpoint()
        serializer = AccountSerializer(instance=account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
