"""restframework_test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={
            'template_name' : 'login.html'
            }
        ),

    url(r'^accounts/logout/',
        'django.contrib.auth.views.logout',
        name='logout'),

    url(r'^moim_list/',
        'but_moim.views.moim_list',
         name='moim_list'),

    url(r'^moim_detail/(?P<moim_name>[\w.@+-]+)/$',
        'but_moim.views.moim_detail',
         name='moim_detail'),

    url(r'^moim_join/',
        'but_moim.views.moim_join',
         name='moim_join'),

    url(r'^moim_search/',
        'but_moim.views.moim_search',
         name='moim_search'),

    url(r'^moim_search_join/(?P<moim_name>[\w.@+-]+)/$',
        'but_moim.views.moim_search_join',
         name='moim_search_join'),


]
