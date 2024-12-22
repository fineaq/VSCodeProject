from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')

def main(request):
    return render(request, 'Bookstore_App/main.html')
