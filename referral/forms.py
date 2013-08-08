# coding=utf-8
"""
Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports
from django.forms import ModelForm

# 3rd party imports

# Local imports
from models import Link


class NewLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ('title', )


class EditLinkForm(ModelForm):
    class Meta:
        model = Link