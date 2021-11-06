from django.db import models

from movies.models import Movie


class Poster(models.Model):
    movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE, verbose_name='Название фильма')
    date = models.DateTimeField(verbose_name='Время сеанса')
