from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model for posting recipes
class Recipe_Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    description = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Recipe_Post, on_delete=CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="commenter")
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)