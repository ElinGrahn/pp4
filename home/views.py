from django.shortcuts import render
from django.views import generic
from .models import Recipe_Post

# Create your views here.
class PostList(generic.ListView):
    model = Recipe_Post
    template_name = 'recipe_post_list.html'