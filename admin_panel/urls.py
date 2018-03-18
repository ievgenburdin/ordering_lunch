from django.conf.urls import url

from admin_panel import views


urlpatterns = ([
    url(r'^import/$', views.ImportView.as_view(), name='import'),
    url(r'^$', views.UsersListView.as_view(), name='users_list'),
    url(r'^food/$', views.FoodListView.as_view(), name='food_list'),
], 'admin_panel')