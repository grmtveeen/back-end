from django.db import models


class Poster(models.Model):
    date = models.DateTimeField(verbose_name='Время сеанса')
