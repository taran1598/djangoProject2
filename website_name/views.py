from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


# Create your views here.
from data_loader.models import FoodName


def index(request):
    return render(request, 'website_name/index.html')


def ingredient(request):
    return render(request, 'website_name/ingredient.html')


def search_ingredients(request):

    if request.method == 'POST':
        search_input = request.POST.get('search_input')
        food_names = FoodName.objects.filter(food_desc__contains=search_input)
        return render(request, 'website_name/search_ingredients_results.html', {'search_input': search_input,
                                                                                'food_names': food_names})
    else:
        return render(request, 'website_name/search_ingredients_results.html')
