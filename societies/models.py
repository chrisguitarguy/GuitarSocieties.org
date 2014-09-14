# -*- coding: utf-8 -*-
"""
societies.models
~~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: Proprietary
"""

from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _


class GuitarSociety(models.Model):
    """
    Represents a single guitar society.

    .. versionadded:: 0.1
    """

    class Meta:
        verbose_name_plural = _('Guitar Societies')

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


class Issue(models.Model):
    """
    Represents a "issue" with a guitar society -- reporting a problem, etc.

    .. versionadded:: 0.1
    """

    class Meta:
        ordering = ['-created']

    BROKEN_LINK = 'link'
    INCORRECT_NAME = 'name'
    INCORRECT_REGION = 'region'
    CUSTOM_ISSUE = 'custom'
    TYPE_CHOICES = (
        (BROKEN_LINK, _('Broken Link')),
        (INCORRECT_NAME, _('Incorrect Name')),
        (INCORRECT_REGION, _('Incorrect Region')),
        (CUSTOM_ISSUE, _('Custom')),
    )

    #: the society to which the issue belongs
    #: .. versionadded:: 0.1
    society = models.ForeignKey(GuitarSociety, on_delete='CASCADE')

    #: What kind of issue we're ding with
    #: .. versionadded:: 0.1
    issue_type = models.CharField(max_length=12, choices=TYPE_CHOICES, default=CUSTOM_ISSUE)

    #: A longer description of the issue, maybe be blank
    #: .. versionadded:: 0.1
    description = models.TextField(null=True, blank=True, default=None)

    #: When the issue was created
    #: .. versionadded:: 01
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.issue_type, self.society)

    def __repr__(self):
        return '<Issue("{}", {})>'.format(self.issue_type, repr(self.society))
