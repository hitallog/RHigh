from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Vaga

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class VagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaga
        fields = ('vaga', 'desc', 'salario')