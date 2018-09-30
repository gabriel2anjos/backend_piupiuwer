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

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email', 'password')

    def create(self, validated_data):
        user = super(UsersSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

