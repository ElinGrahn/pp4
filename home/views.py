from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe_Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe_Post.objects.filter(title=1)
    template_name = 'base.html'

def recipes(request):
    
    queryset = Post.objects.filter(last=1)
    post = get_object_or_404(queryset)

    return render(
        request,
        "blog/recipes.html",
        {"post": post},
    )

def favourites(request):

    queryset = Post.objects.filter(title=1)
    post = get_object_or_404(queryset)

    return render(
        request,
        "blog/favourites.html",
        {"post": post},
    )

def register(request):
   
    queryset = Post.objects.filter(title=1)
    post = get_object_or_404(queryset)

    return render(
        request,
        "blog/register.html",
        {"post": post},
    )

def login(request):
    
    queryset = Post.objects.filter(title=1)
    post = get_object_or_404(queryset)

    return render(
        request,
        "blog/login.html",
        {"post": post},
    )

def recipe_detail(request):
    
    queryset = Post.objects.filter(title=1)
    post = get_object_or_404(queryset)

    return render(
        request,
        "blog/recipe_detail.html",
        {"post": post},
    )