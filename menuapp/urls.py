from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipe/(?P<recipe_id>\w{0,50})/$', views.recipe, name='recipe'),
]