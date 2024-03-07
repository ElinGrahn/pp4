from django.contrib import admin
from .models import Recipe_Post
from .models import Comment

# Register your models here.
admin.site.register(Recipe_Post)
admin.site.register(Comment)