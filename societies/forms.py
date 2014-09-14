# -*- coding: utf-8 -*-
"""
societies.forms
~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: Proprietary
"""

from django import forms
from .models import Issue


class SubmitIssueForm(forms.ModelForm):
    """
    Frontend form for reporting an issue with a guitar society.

    .. versionadded:: 0.1
    """

    class Meta:
        model = Issue
        fields = ('issue_type', 'description',)
