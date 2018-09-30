from django.conf.urls import url, include
from api.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token, obtain_jwt_token
from rest_framework import generics
from piu.models import *
from api.serializers import *

router = DefaultRouter()
# router.register(r'pius', PiusViewset.as_view())
# router.register(r'usuarios',UsuariosViewset.as_view())

urlpatterns = [
    url(r'^login/$', obtain_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^usuarios/', UsuariosViewset.as_view()),
    url(r'^pius/', PiusViewset.as_view()),
    
]

urlpatterns += router.urls
