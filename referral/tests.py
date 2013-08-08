# coding=utf-8
"""
Referral Tests.

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports

# 3rd party imports
import pytest

# Local imports
from models import Link


@pytest.mark.django_db
def test_link_model():
    link = Link.objects.create(title='test_link')
    link.save()

    assert link.clicks == 0