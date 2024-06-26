from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipe_list, name='recipe_list'),# All Recipe page
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'), 
    path('recipe/new/', views.recipe_create, name='recipe_create'),
    path('about/', views.about, name='about'),  # About Us page
]