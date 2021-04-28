from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Rockslide Portal")

def top(request):
    return redirect('/portal/')
