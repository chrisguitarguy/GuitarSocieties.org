from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _('Guitar Societies')
admin.site.site_title = _('Guitar Societies')
admin.site.index_title = _('Guitar Society Admin')

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('societies.urls', namespace='societies')),
)
