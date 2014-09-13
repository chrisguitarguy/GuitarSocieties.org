# -*- coding: utf-8 -*-
"""
societies.urls
~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: Proprietary
"""

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<country>[a-z]{2})$', views.country, name='country'),
    url(r'^(?P<socid>\d+)$', views.single, name='single'),
)
