from django.urls import path
from . import views

app_name = 'website_name'
urlpatterns = [
    path('', views.index, name='index'),
    path('ingredient/', views.ingredient, name='ingredient'),
    path('results/', views.search_ingredients, name='results')
]
