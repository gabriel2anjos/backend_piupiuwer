from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from piu.models import *
from api.serializers import *
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from .serializers import UserSerializer
from rest_framework.views import APIView, Response

# Create your views here.

class PiusViewset(generics.ListCreateAPIView):
    # queryset = Piu.objects.all()
    """
    get:
    Retorna uma lista de pius.

    post:
    Cria um novo piu que pode ter os seguintes atributos:
    """
    serializer_class = PiuSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Piu.objects.all()
        usuario = self.request.query_params.get('usuario', None)
        if usuario is not None:
            queryset = queryset.filter(usuario=usuario)
        return queryset

class UsuariosViewset(generics.ListAPIView):
     """
     Retorna uma lista com todos os usuarios.
     """
     queryset = User.objects.all()
     serializer_class = UsuarioSerializer

class UsersViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UsuarioSerializer