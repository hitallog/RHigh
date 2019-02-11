from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from rhfun import views as core_views

urlpatterns = [
    url(r'', include('rhfun.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),  
    url('', TemplateView.as_view(template_name='home.html'), name='home'), 
    

 
]
