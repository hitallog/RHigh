from api.v1.serializers import UserSerializer, VagaSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

from rhfun.models import Vaga


class VagasViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

