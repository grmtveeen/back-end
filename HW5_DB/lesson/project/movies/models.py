from django.db import models
from genres.models import Genre


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=64)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
