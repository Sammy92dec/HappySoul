from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Recipe


class RecipeForm(forms.ModelForm):
    """ Recipe Form"""
    class Meta:
        model = Recipe
        fields = [
            'title', 
            'description', 
            'ingredients', 
            'image', 
            'image_alt', 
            'meal_type'
        ]

        
        ingredients = forms.CharField(widget=SummernoteWidget())
        instructions = forms.CharField(widget=SummernoteWidget())

        widgets = {
            'description': forms.Textarea(attrs={'row': 5}), 
        }

        labels = {
            'title': 'Title',
            'description': 'Description', 
            'ingredients': 'Recipe Ingredients',
            'image': 'Recipe Image',
            'image_alt': 'Describe Image',
            'meal_type': 'Meal Type',
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields[
            'body'
            ].label = ""
            