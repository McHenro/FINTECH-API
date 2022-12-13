from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import DepositCreateAPISerializer, AccountSerializer, WithdrawCreateAPISerializer
from rest_framework.response import Response



class DepositCreateAPI(generics.CreateAPIView):
    
    permission_classes = (IsAuthenticated,)
    
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
