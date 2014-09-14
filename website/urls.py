from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^societies/', include('societies.urls', namespace='societies')),
)
