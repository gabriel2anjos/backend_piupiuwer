from django.conf.urls import url, include
from api.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token, obtain_jwt_token
from rest_framework import generics
from piu.models import *
from api.serializers import *

router = DefaultRouter()
router.register(r'registrar', UsersViewset)
# router.register(r'pius', PiusViewset.as_view())
# router.register(r'usuarios',UsuariosViewset.as_view())

urlpatterns = [
    url(r'^login/$', obtain_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^usuarios', UsuariosViewset.as_view()),
    url(r'^registrar', CreateUserView.as_view()),
    url(r'^pius/(?P<pk>\d+)/$', PiusRUDViewset.as_view()),
    url(r'^pius/', PiusCLView.as_view()),
    url(r'^docs/', include_docs_urls(title='PiuPiuwer')),
    #url(r'^registrar/^', UsersViewset.as_view())
    
]

urlpatterns += router.urls
