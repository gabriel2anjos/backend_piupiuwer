from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from piu.models import *
from perfil.models import Perfil

class PiuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piu
        fields = '__all__'
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email',)

    # def create(self, validated_data):
    #     user = super(UsersSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     Perfil.objects.create(user=user.pk)
    #     return user

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Perfil.objects.create(user=user)

        return user

    foto_perfil = serializers.SerializerMethodField('getter_foto_perfil')
    def getter_foto_perfil(self, user):
        return user.perfil_relacionado.foto_perfil

    class Meta:
        model = User
        fields = ['id','username','password','first_name','last_name','email','foto_perfil']
