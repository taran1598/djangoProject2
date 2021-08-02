from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'website_name/index.html')


def ingredient(request):
    return render(request, 'website_name/ingredient.html')


def search(request):
    return render(request, 'website_name/index.html')
