from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('recipes/', recipes, name='recipes'),
    path('favourites/', favourites, name='favourites'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]