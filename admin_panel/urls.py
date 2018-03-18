from django.conf.urls import url

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from admin_panel import views


urlpatterns = ([
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin_panel:users_list')), name='admin_panel'),
    url(r'^import/$', views.ImportView.as_view(), name='import'),
    url(r'^users/$', views.UsersListView.as_view(), name='users_list'),
    url(r'^food/$', views.FoodListView.as_view(), name='food_list'),
], 'admin_panel')