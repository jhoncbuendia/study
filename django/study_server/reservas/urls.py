"""study_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from reservas.api import views
#from services import urls as services_url (?P<product>\w+)/
urlpatterns = [
    url(r'^$', views.ReservaList.as_view({ 'get':'list', 'post':'create'})),
    url(r'^(?P<pk>\w+)/$', views.ReservaDetail.as_view({ 'put':'update'})),

]
