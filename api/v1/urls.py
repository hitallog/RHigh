from rest_framework import routers
from api.v1 import views
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'vagas', views.VagasViewSet)

urlpatterns = [

    path('login', views.login),

    path('', include(router.urls)),

]
