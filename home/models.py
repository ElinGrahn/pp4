from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model for posting recipes
class Recipe_Post(models.Model):
    title = models.CharField(max_length=200, uniqe=True)
    slug = models.SlugField(max_length=200, uniqe=True)
    author = models.ForeignKey(User, on_delete.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    description = models.TextField()