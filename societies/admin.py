# -*- coding: utf-8 -*-
"""
societies.admin
~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: http://opensource.org/licenses/bsd-3-clause
"""

from django.contrib import admin
from .models import GuitarSociety, Issue


class IssueInline(admin.TabularInline):
    model = Issue
    extra = 0
    readonly_fields = ('created',)


class GuitarSocietyAdmin(admin.ModelAdmin):
    """
    Customizes some display things for guitar societies in the admin area.

    .. versionadded:: 0.1
    """
    list_display = ('name', 'link',)
    readonly_fields = ('created',)
    inlines = [IssueInline]


admin.site.register(GuitarSociety, GuitarSocietyAdmin)
