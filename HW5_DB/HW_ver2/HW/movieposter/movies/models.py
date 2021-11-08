from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название', null=False)
    main_actor = models.ForeignKey(Actor, null=False, on_delete=models.SET_DEFAULT, default=0,
                                   verbose_name='Главный актер')
    genre = models.ForeignKey(Genre, null=False, on_delete=models.SET_DEFAULT, default=0,
                              verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год', default=0, null=False)
    link = models.CharField(max_length=64, verbose_name='Ссылка на трейлер', null=False)
    img = models.CharField(max_length=64, verbose_name='Ссылка на static img', null=False)
    description = models.TextField(verbose_name='Описание фильма', null=False)