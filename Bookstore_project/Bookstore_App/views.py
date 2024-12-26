from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *


def home(request):
    return HttpResponse('home')

def main(request):
    return render(request, 'Bookstore_App/main.html')

def login(request):
    return render(request, 'Bookstore_App/login.html')