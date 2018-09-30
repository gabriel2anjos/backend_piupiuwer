from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from piu.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']

class PiuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piu
        fields = '__all__'

