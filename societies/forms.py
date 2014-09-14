# -*- coding: utf-8 -*-
"""
societies.forms
~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: http://opensource.org/licenses/bsd-3-clause
"""

from django import forms
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from .models import Issue


class SubmitIssueForm(forms.ModelForm):
    """
    Frontend form for reporting an issue with a guitar society.

    .. versionadded:: 0.1
    """

    class Meta:
        model = Issue
        fields = ('issue_type', 'description',)

    def clean(self):
        cleaned = super().clean()
        typ = cleaned.get('issue_type')
        desc = cleaned.get('description')
        if Issue.CUSTOM_ISSUE == typ and not desc:
            self.add_error('description', _('Please describe the issue.'))

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return strip_tags(description) if description else None
