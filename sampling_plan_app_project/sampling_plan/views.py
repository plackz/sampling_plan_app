"""
# defualt file from django
from django.shortcuts import render

# Create your views here.
"""
from django.http import HttpResponse

def index(request):
    return HttpResponse("Boilerplate to start with")
