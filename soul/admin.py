from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
# Admins Recipe model features 
class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        'title', 
        'meal_type', 
        'status',
        'vegan',
        'vegetarian'
        )

    search_fields = ['title', 'meal_type']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Admins Comment model features
    list_display = ('name', 'body', 'recipe', 'created_on')
    search_fields = ('name', 'email', 'body')
    list_filter = ('created_on',)