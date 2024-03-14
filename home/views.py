from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe_Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe_Post.objects.filter(title=1)
    template_name = 'index.html'

def recipes(request):
    recipes = Recipe_Post.objects.all()
    return render(request, "recipes.html", {"Recipes": recipes})

def favourites(request):
    recipes = Recipe_Post.objects.all()
    return render(request, "favourites.html", {"favourites": recipes})

def recipe_detail(request):
    recipes = Recipe_Post.objects.all()
    return render(request, "recipe_detail.html", {"Recipe_detail": recipes})


def register(request):
    recipes = Recipe_Post.objects.all()
    return render(request, "register.html", {"register": form})

def login(request):
    recipes = Recipe_Post.objects.all()
    return render(request, "login.html", {"login": form})
