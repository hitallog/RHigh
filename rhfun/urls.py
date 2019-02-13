from django.views.generic.base import TemplateView
from django.conf.urls import url
from rhfun import views


urlpatterns = [
    url(r'^cadastrar/', views.cadastrar, name='cadastrar'),
    url(r'^vagas/', views.ver_vagas, name='vagas'),
    url(r'^cadastrar_curriculo/', views.cadastrar_curriculo, name='cadastrar_curriculo'),
    url(r'^cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    url(r'^signup/', views.signup, name='signup'),
    
    # ex: /vagas/5/detail/
    url(r'^(?P<vaga_id>[0-9]+)/detail/$', views.detail, name='detail'),

    url('', TemplateView.as_view(template_name='../templates/rhfun/home.html'), name='home'),

]
