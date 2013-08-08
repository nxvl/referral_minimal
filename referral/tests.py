# coding=utf-8
"""
Referral Tests.

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports
from django.test import Client

# 3rd party imports
import pytest

# Local imports
from models import Link


@pytest.mark.django_db
def test_link_model():
    link = Link.objects.create(title='test_link')
    link.save()

    assert link.clicks == 0


@pytest.mark.django_db
def test_add_link():
    c = Client()

    assert Link.objects.count() == 0

    response = c.post('/', {'title': 'test_link'})

    assert response.status_code == 200
    assert response.templates[0].name == 'home.html'

    assert Link.objects.count() == 1

    assert [x for x in response.context[0].dicts[9]['links']] == \
           [x for x in Link.objects.all()]


@pytest.mark.django_db
def test_landing_page():
    c = Client()

    c.post('/', {'title': 'test_link'})

    assert Link.objects.all()[0].clicks == 0

    response = c.get('/landing/', {'link': 'test_link'})

    assert Link.objects.all()[0].clicks == 1
    assert response.status_code == 200
    assert response.templates[0].name == 'landing.html'
    assert response.context[0].dicts[9]['title'] == 'test_link'

    response = c.get('/landing/')

    assert response.status_code == 404

    response = c.get('/landing/', {'link': 'bad_link'})

    assert response.status_code == 404


@pytest.mark.django_db
def test_edit_link():
    c = Client()

    c.post('/', {'title': 'test_link'})

    response = c.get('/edit/1/')

    assert response.status_code == 200
    assert response.templates[0].name == 'edit.html'

    response = c.post('/edit/1/', {'title': 'foo', 'clicks': 100})

    assert response.status_code == 302

    links = Link.objects.all()

    assert links.count() == 1
    assert links[0].title == 'foo'
    assert links[0].clicks == 100


@pytest.mark.django_db
def test_delete_link():
    c = Client()

    c.post('/', {'title': 'test_link'})

    response = c.get('/delete/1/')

    assert response.status_code == 302
    assert not Link.objects.all()