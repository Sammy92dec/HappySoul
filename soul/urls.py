from . import views
from django.urls import path
from .views import AddRecipe

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add-recipe/', views.add_recipe, name='add_recipe')
]