from django.http import Http404
from django.shortcuts import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def error(request, *args, **kwargs):
    return Http404