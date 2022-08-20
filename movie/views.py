from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Welcome to the Home Page</h1>')

def about(request):
  return HttpResponse('<h1>Welcome to our About Page</h1>')
