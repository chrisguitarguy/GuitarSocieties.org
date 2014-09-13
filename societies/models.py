# -*- coding: utf-8 -*-
"""
societies.models
~~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: Proprietary
"""

from django.db import models
from django_countries.fields import CountryField


class GuitarSociety(models.Model):
    """
    Represents a single guitar society.

    .. versionadded:: 0.1
    """

    #: the name of the society
    #: ..versionadded:: 0.1
    name = models.CharField(max_length=1024)

    #: the society's url
    #: ..versionadded:: 0.1
    link = models.URLField(max_length=255)

    #: The country in which the society resides
    #: .. versionadded:: 0.1
    country = CountryField()

    #: A free form "city" or "region" field used to display where
    #: exactly the society is within a country
    #: .. versionadded:: 0.1
    region = models.CharField(max_length=512, null=True, default=None, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<GuitarSociety("{}")>'.format(self.name)
