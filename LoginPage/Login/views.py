from django.http import HttpResponse
from django.shortcuts import render

def homepage_name(request):
    return HttpResponse('HOME PAGE')

def secondpage_name(request):
    return HttpResponse('SECOND PAGE')
