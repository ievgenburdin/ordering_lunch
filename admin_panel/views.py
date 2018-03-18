from django.shortcuts import render

from django.views.generic import TemplateView


class ImportView(TemplateView):
    template_name = 'admin_panel/import.html'


class UsersListView(TemplateView):
    template_name = 'admin_panel/users_list.html'


class FoodListView(TemplateView):
    template_name = 'admin_panel/food_list.html'


