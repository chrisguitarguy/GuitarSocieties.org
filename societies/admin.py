# -*- coding: utf-8 -*-
"""
societies.admin
~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: Proprietary
"""

from django.contrib import admin
from .models import GuitarSociety


class GuitarSocietyAdmin(admin.ModelAdmin):
    """
    Customizes some display things for guitar societies in the admin area.

    .. versionadded:: 0.1
    """
    list_display = ('name', 'link',)


admin.site.register(GuitarSociety, GuitarSocietyAdmin)
