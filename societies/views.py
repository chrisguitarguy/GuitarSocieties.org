# -*- coding: utf-8 -*-
"""
societies.views
~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: http://opensource.org/licenses/bsd-3-clause
"""

from collections import OrderedDict
import urllib.parse as urlparse
from django.contrib import messages
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.utils.translation import ugettext_lazy as _
from django_countries import countries
from .forms import SubmitIssueForm
from .models import GuitarSociety, Issue


def _get_all_societies():
    all_societies = GuitarSociety.objects.filter(active=True).order_by('country', 'region')
    societies = OrderedDict()
    for soc in all_societies:
        societies.setdefault(soc.country, list()).append(soc)
    return societies


def _get_society(socid):
    return get_object_or_404(GuitarSociety, pk=socid, active=True)


def index(request):
    """
    Show every guitar society in our database.

    .. versionadded:: 0.1

    :param request: the django request object
    """
    societies = _get_all_societies()

    return render(request, 'societies/index.html', {
        'all_societies': societies,
    })


def country(request, country):
    societies = get_list_or_404(GuitarSociety.objects.filter(active=True), country=country.upper())
    country = societies[0].country

    return render(request, 'societies/country.html', {
        'societies': societies,
        'all_societies': _get_all_societies(),
        'country': country
    })


def issue(request, socid):
    society = _get_society(socid)
    issue = Issue(society=society)
    if 'POST' == request.method:
        form = SubmitIssueForm(request.POST, instance=issue)
        if form.is_valid():
            issue.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                _('Issue reported! Thank you.'),
                extra_tags='success',
            )
            return redirect('societies:index')
    else:
        form = SubmitIssueForm(instance=issue)

    return render(request, 'societies/issue.html', {
        'society': society,
        'form': form,
        'all_societies': _get_all_societies(),
    })


def single(request, socid):
    society = _get_society(socid)
    scheme, netloc, path, query, frag = urlparse.urlsplit(society.link)
    query = urlparse.parse_qs(query, keep_blank_values=True)
    query.update({
        'utm_source': 'guitarsocieties.org',
        'utm_medium': 'website',
        'utm_campaign': 'guitarsocieties',
    })
    return redirect(urlparse.urlunsplit((
        scheme,
        netloc,
        path,
        urlparse.urlencode(query, doseq=True),
        frag,
    )))
