"""
Definition of urls for Inz.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from psw.forms import pswAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'psw.views.home', name='home'),
    url(r'^servers/', 'psw.views.servers', name='servers'),
    url(r'^psw/servers/', 'psw.views.servers', name='servers'),
    url(r'^listservers/', 'psw.views.listservers', name='listservers'),
    url(r'^register/', 'psw.views.register', name='register'),
    url(r'^login/$', 'psw.views.login_view', name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
