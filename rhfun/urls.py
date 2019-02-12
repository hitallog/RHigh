from django.views.generic.base import TemplateView
from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from rhfun import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'vagas', views.VagasViewSet)

urlpatterns = [
    url(r'^cadastrar/', views.cadastrar, name='cadastrar'),
    url(r'^vagas/', views.ver_vagas, name='vagas'),
    url(r'^cadastrar_curriculo/', views.cadastrar_curriculo, name='cadastrar_curriculo'),
    url(r'^cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^filme/', views.filme, name='filme'),
    
    # ex: /vagas/5/detail/
    url(r'^(?P<vaga_id>[0-9]+)/detail/$', views.detail, name='detail'),

    path('api/', include(router.urls)),

    url('', TemplateView.as_view(template_name='home.html'), name='home'),

]