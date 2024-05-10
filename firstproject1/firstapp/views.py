from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    s='<h1>WELCOME TO DJANGO</h1>'
    return HttpResponse(s)