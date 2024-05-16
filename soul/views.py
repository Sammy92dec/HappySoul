from django.views.generic import CreateView, UpdateView 
from .models import Recipe
from django.views import generic
from django.urls import reverse_lazy
from .form import RecipeForm


class AddRecipe(CreateView):
    """ Add recipes """

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_message = 'Recipe Successfully Added'
    success_url = '/recipes/'

def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe).form_valid(form)



# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6









    

class EditRecipe(UpdateView):
    """Edits recipe"""
    model = Recipe
    template_name = ''
    success_message = 'Recipe Successfully Updated'
    success_url = reverse_lazy('your_recipes')    