from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),  
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'', include('rhfun.urls')),

 
]
