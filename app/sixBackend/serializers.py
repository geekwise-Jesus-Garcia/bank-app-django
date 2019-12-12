from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class Bankserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Bank
        fields = ['bank_name', ]

class Accountserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Account
        fields = []
