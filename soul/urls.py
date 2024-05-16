from . import views
from django.urls import path
from .views import AddRecipe

urlpatterns = [
    path('#', views.PostList.as_view(), name='home'),
    path('', AddRecipe.as_view(), name='add_recipe'),
]