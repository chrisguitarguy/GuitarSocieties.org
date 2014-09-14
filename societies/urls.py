# -*- coding: utf-8 -*-
"""
societies.urls
~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: http://opensource.org/licenses/bsd-3-clause
"""

from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^country/(?P<country>[a-z]{2})$', views.country, name='country'),
    url(r'^issue/(?P<socid>\d+)$', views.issue, name='issue'),
    url(r'^go/(?P<socid>\d+)$', views.single, name='single'),
)
