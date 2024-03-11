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
    save = models.BooleanField(User, default=False)


class save(models.Model): 
    save = models.ManyToManyField(User, related_name='saved_recipes')

    def __str__(self):
        return f"Saves: "

class Comment(models.Model):
    post = models.ForeignKey(Recipe_Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"