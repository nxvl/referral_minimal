# coding=utf-8
"""
Referral Tests.

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports
from django.conf.urls import patterns, include, url
from django.contrib import admin

# 3rd party imports

# Local imports


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'referral.views.home', name='home'),
    url(r'^landing/', 'referral.views.landing', name='landing'),

    url(r'^admin/', include(admin.site.urls)),
)
