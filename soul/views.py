from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView, UpdateView 
from .models import Recipe
from django.urls import reverse_lazy



# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

class AddRecipe(CreateView):
    """ Add recipes """
    template_name = "templates/add_recipe.html"
    model = Recipe
    success_message = 'Recipe Successfully Added'
    success_url = reverse_lazy('your_recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditRecipe(UpdateView):
    """Edits recipe"""
    model = Recipe
    template_name = ''
    success_message = 'Recipe Successfully Updated'
    success_url = reverse_lazy('your_recipes')    