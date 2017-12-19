from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'categories/$', views.CategoryList.as_view()),
    url(r'weeks/$', views.WeekList.as_view()),
    url(r'weeks/(?P<week_id>\w{0,50})/$', views.WeekDetail.as_view()),
    url(r'recipes/$', views.RecipeList.as_view()),
    url(r'recipes/(?P<recipe_id>\w{0,50})/$', views.RecipeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
