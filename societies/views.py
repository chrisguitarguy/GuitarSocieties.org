# -*- coding: utf-8 -*-

import urllib.parse as urlparse
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django_countries import countries
from .models import GuitarSociety


def index(request):
    """
    Show every guitar society in our database.

    .. versionadded:: 0.1

    :param request: the django request object
    """
    all_societies = GuitarSociety.objects.all().order_by('country', 'region')
    societies = dict()
    for soc in all_societies:
        societies.setdefault(soc.country, list()).append(soc)

    return render(request, 'societies/index.html', {
        'all_societies': societies,
    })


def country(request, country):
    societies = get_list_or_404(GuitarSociety, country=country.upper())
    country = societies[0].country

    return render(request, 'societies/country.html', {
        'societies': societies,
        'country': country
    })


def single(request, socid):
    society = get_object_or_404(GuitarSociety, pk=socid)
    scheme, netloc, path, query, frag = urlparse.urlsplit(society.link)
    query = urlparse.parse_qs(query, keep_blank_values=True)
    query.update({
        'utm_source': 'classicalguitar.org',
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
