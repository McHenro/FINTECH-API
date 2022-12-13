from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.db import transaction

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    
    
    
class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    
    class Meta:
        model = Account
        fields = '__all__'
        
    def get_owner(self, obj):
        return obj.owner.first_name +' '+ obj.owner.last_name
        
    
class DepositCreateAPISerializer(serializers.Serializer):
    amount = serializers.FloatField(required=True)
    account = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        errors = {}
        # verify that appt amount is the amount set by the doctor
        amount = attrs['amount']
        account = attrs['account']
        
        if not amount or amount < 100.00:
            errors['amount'] = 'Please enter a valid amount'
        if account:
            try:
                account = Account.objects.get(pk=account)
            except Account.DoesNotExist:
                errors['Account'] = 'This Account does not exist'
                
        if errors:
            raise serializers.ValidationError(errors)

        return attrs
    
    @transaction.atomic
    def create(self, validated_data):
        account_id = validated_data.get('account')
        amount = validated_data.get('amount')
        
        account = Account.objects.get(pk=account_id)
        
        account.balance += amount 
        account.save()
        
        Deposit.objects.create(amount=amount, account=account)
        
        return account


class WithdrawCreateAPISerializer(serializers.Serializer):
    amount = serializers.FloatField(required=True)
    account = serializers.IntegerField(required=True)
    
    def validate(self, attrs):
        errors = {}
        amount = attrs['amount']
        account_id  = attrs['account']
        breakpoint()
        
        if amount < 1000.00:
            errors['amount'] = 'Please you can only withdraw above 1000 '
        if account_id:
            try:
                account = Account.objects.get(pk=account_id)
                if account.balance <= 0.00:
                    errors['amount'] = 'Insuffucuent fund, Please fund your account'
                withdrawee_id = self.context['request'].user.id
                # breakpoint()
                if withdrawee_id != account.owner.id:
                    breakpoint()
                    errors['detail'] = 'This Account does not belong to you'
            except Account.DoesNotExist:
                errors['detail'] = 'This Account does not exist'
        if errors:
            raise serializers.ValidationError(errors)

        return attrs
    
    @transaction.atomic
    def create(self, validated_data):
        account_id = validated_data.get('account')
        amount = validated_data.get('amount')
        account = Account.objects.get(pk=account_id)
        
        account.balance -= amount 
        account.save()
        
        Withdraw.objects.create(amount=amount, account=account)
        
        return account