from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
# from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

   



