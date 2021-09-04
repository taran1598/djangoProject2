from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from data_loader.models import FoodName
from website_name.nutrition_label_builder import NutrientLabelBuilder


def index(request):
    return render(request, 'website_name/index.html')


def ingredient(request, food_id):
    nutrition_label_builder = NutrientLabelBuilder(food_id=food_id)
    try:
        nutrition_info_dict = nutrition_label_builder.nutrition_label_builder()
        context = {'nutrition': nutrition_info_dict,
                   'food_desc': nutrition_label_builder.food_desc}
        return render(request, 'website_name/ingredient.html', context=context)
    except FoodName.DoesNotExist:
        # return error saying the food item doesn't exist
        return render(request, 'website_name/ingredient.html')


def search_ingredients(request):
    if request.method == 'POST':
        search_input = request.POST.get('search_input')
        food_names = FoodName.objects.filter(food_desc__icontains=search_input)
        return render(request, 'website_name/search_ingredients_results.html', {'search_input': search_input,
                                                                                'food_names': food_names})
    else:
        return render(request, 'website_name/search_ingredients_results.html')
