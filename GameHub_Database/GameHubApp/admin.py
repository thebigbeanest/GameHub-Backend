from django.contrib import admin
from .models import Game, Review, Comment
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
admin.site.register(Review)
admin.site.register(Comment)
