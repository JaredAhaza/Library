from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, we welcome you to our services that allows you to have better library management services.")
