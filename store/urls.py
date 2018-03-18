from django.conf.urls import url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from store import views

urlpatterns = ([
    url(r'^$', RedirectView.as_view(url=reverse_lazy('store:food_list')), name='home'),
    url(r'^food/$', views.FoodListView.as_view(), name='food_list'),
    url(r'^basket/$', views.BasketView.as_view(), name='basket'),
], 'store')