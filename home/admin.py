from django.contrib import admin
from .models import Recipe_Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe_Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title']
    summernote_fields = ('ingredients', 'instructions', 'description',)

# Register your models here.
admin.site.register(Comment)