from django.contrib import admin

from django.contrib import admin
from .models import Game, Review, Comment
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Comment)
