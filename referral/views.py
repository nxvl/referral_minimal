# coding=utf-8
"""
Referral Views.

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# 3rd party imports

# Local imports
from forms import LinkForm
from models import Link


def home(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()

    form = LinkForm()

    links = Link.objects.all()

    data = {
        'links': links,
        'form': form
    }

    return render(request, 'home.html', data)


def landing(request):
    title = request.GET.get('link', '')

    if not title:
        raise Http404

    link = get_object_or_404(Link, title=title)
    link.clicks += 1
    link.save()

    data = {
        'title': title
    }

    return render(request, 'landing.html', data)