from django.db import models
from django.utils import timezone

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    html_code = models.TextField(blank=True)
    css_code = models.TextField(blank=True)
    js_code = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    game = models.ForeignKey(Game, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Can update this to grab user data later

class Comment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Can update this to add user data / 'reply to' functions later

    