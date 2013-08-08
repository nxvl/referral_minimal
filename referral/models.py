# coding=utf-8
"""
Referral Models.

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports
from django.db import models

# 3rd party imports

# Local imports


class Link(models.Model):
    title = models.CharField(max_length=20, verbose_name="Link Title")
    clicks = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
