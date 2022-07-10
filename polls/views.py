from django.shortcuts import render
# Protocolo de redireccionamiento
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")