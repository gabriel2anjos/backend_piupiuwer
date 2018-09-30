from django.shortcuts import render
from rest_framework import generics
from piu.models import *
from api.serializers import *

from rest_framework.views import APIView, Response

# Create your views here.

class PiusViewset(generics.ListCreateAPIView):
    # queryset = Piu.objects.all()
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

class UsuariosViewset(generics.ListCreateAPIView):
     queryset = User.objects.all()
     serializer_class = UsuarioSerializer