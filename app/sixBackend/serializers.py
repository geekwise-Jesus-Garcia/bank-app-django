from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Bank, Account, Customer, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Bank
        fields = ['bank_name' ]

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Account
        fields = ['account_options', 'username', 'email', 'options']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Customer
        fields = ['customer_name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Product
        fields = ['product_option', 'option']


