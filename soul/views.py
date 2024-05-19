from .form import RecipeForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment, Like


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html',{'recipes':recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.autor = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', pk=pk)

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save
            return redirect('recipe_detail', pk=recipe.pk)
    
    else :
        form = RecipeForm()
    return  render(request, 'recipe/recipe_form.html',{'form': form})