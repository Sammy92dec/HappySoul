from .models import Comment, Recipe
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login', css_class='btn-primary'))
"""
class RecipeForm(forms.ModelForm):
    Recipe Form
    class Meta:
        model = Recipe
        fields = (
            'title', 'description', 'ingredients', 'method',
            'vegetarian', 'vegan', 'image', 'image_url'
            )
        
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
        }"""