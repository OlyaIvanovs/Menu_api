from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^recipeslist$', views.RecipeList.as_view()),
    url(r'^categorieslist$', views.CategoryList.as_view()),
    url(r'^recipe/(?P<recipe_id>\w{0,50})/$', views.RecipeAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
