from os import fdopen

from django.contrib import admin
from .models import Category, VideoContent, Comment, Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(VideoContent)
admin.site.register(Comment)
admin.site.register(Profile)
