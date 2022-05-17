from django.db import models
from django.conf import settings

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.URLField()
    release_date = models.DateField()
    wished_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movie_list')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


class Actor(models.Model):
    name = models.CharField(max_length=20)
    character = models.CharField(max_length=20)
    profile_path = models.URLField()
    actor_movies = models.ManyToManyField(Movies, related_name='movie_actors')


class Director(models.Model):
    name = models.CharField(max_length=20)
    profile_path = models.URLField()
    director_movies = models.ManyToManyField(Movies, related_name='movie_directors')


class Genre(models.Model):
    name = models.CharField(max_length=20)
    genre_movies = models.ManyToManyField(Movies, related_name='movie_genres')