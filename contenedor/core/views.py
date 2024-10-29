from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>WEB PERSONAL</h1><h2>portada</h2>")