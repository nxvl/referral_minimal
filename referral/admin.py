# coding=utf-8
"""
Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports
from django.contrib import admin

# 3rd party imports

# Local imports
from models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'clicks']


admin.site.register(Link, LinkAdmin)