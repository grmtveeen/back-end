from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    main_actor = models.ForeignKey(Actor, null=False, on_delete=models.SET_DEFAULT, default='ERROR, PLS PUT ACTOR',
                                   verbose_name='Главный актер')
    genre = models.ForeignKey(Genre, null=False, on_delete=models.SET_DEFAULT, default='ERROR, PLS PUT GENRE',
                              verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год', default=404)

    link = models.CharField(max_length=64, verbose_name='Ссылка на трейлер')
    img = models.CharField(max_length=64, verbose_name='Ссылка на static img')
    description = models.TextField(verbose_name='Описание фильма')
