from django.views.generic import CreateView, UpdateView 
from .models import Recipe
from django.views import generic
from django.urls import reverse_lazy
from .form import RecipeForm
from django.shortcuts import render



class AddRecipe(CreateView):
    """ Add recipes """

    template_name = "add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_message = 'Recipe Successfully Added'
    success_url = 'add-recipe/'


def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe).form_valid(form)

def add_recipe(request):
    return render(request, 'add_recipe.html')

# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "index.html"
    paginate_by = 6


class EditRecipe(UpdateView):
    """Edits recipe"""
    model = Recipe
    template_name = 'add_recipe.html'
    success_message = 'Recipe Successfully Updated'
    success_url = reverse_lazy('your_recipes')    