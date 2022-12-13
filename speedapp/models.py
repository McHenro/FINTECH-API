from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _




ACCOUNT_TYPE_CHOICE = [
    ('Current', 'Current'), ('Savings', 'Savings'), 
]

BANK_CHOICE = [
    ('First Bank', 'First Bank'), ('Zenith', 'Zenith'), ('Gt Bank', 'Gt Bank')
]


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Owner"))
    account_type = models.CharField(_('Account Type'),max_length=100, choices=ACCOUNT_TYPE_CHOICE)
    bank = models.CharField(_('Bank'),max_length=100, choices=BANK_CHOICE)
    created_at = models.DateTimeField(_('Date Created'),auto_now_add=True)
    balance = models.FloatField(_('Balance'),default = 100000.00)
    
    def __str__(self):
        return str(self.owner)
    
    
class Deposit(models.Model):
    amount = models.FloatField(_('Amount'),)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_("Account"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

class Withdraw(models.Model):
    amount = models.FloatField(_('Amount'),)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_("Account"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    