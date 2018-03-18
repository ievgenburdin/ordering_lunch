from django.shortcuts import render

from django.views.generic import TemplateView


class FoodListView(TemplateView):
    template_name = 'store/food_list.html'


class BasketView(TemplateView):
    template_name = 'store/basket.html'