from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^cadastrar/', views.cadastrar, name='cadastrar'),
    url(r'^vagas/', views.ver_vagas, name='vagas'),
    url(r'^cadastrar_curriculo/', views.cadastrar_curriculo, name='cadastrar_curriculo'),
    url(r'^cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    url(r'^signup/', views.signup, name='signup'),
    
    url(r'^(?P<vaga_id>[0-9]+)/detail/$', views.detail, name='detail'),
    # ex: /vagas/5/results/
    url(r'^(?P<vagas_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /vagas/5/vote/
    url(r'^(?P<vagas_id>[0-9]+)/vote/$', views.vote, name='vote'),
]