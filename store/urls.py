from django.conf.urls import url

from store import views

urlpatterns = ([
    url(r'^$', views.FoodListView.as_view(), name='food_list'),
    url(r'^basket/$', views.BasketView.as_view(), name='basket'),
], 'store')