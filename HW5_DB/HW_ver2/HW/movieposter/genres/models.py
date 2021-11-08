from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=32, verbose_name='Жанр', null=False)
