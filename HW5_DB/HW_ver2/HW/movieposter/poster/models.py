from django.db import models
from movies.models import Movie
from cinemas.models import Cinema

class Poster(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,  default=0, verbose_name='Фильм')
    movie_format = models.CharField(max_length=4, verbose_name='3D/2D/IMAX', default='ERR')
    hall = models.IntegerField(default=-1, verbose_name='Зал')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, default=0, verbose_name='Адрес кинотеатра')
