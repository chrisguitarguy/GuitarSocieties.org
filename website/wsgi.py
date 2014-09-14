# -*- coding: utf-8 -*-
"""
GuitarSocieties.org
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: http://opensource.org/licenses/bsd-3-clause
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
