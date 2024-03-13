from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('favourites/', views.favourites, name='favourites'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]