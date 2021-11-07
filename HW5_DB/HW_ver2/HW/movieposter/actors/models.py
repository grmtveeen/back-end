from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=64, verbose_name='Актер')
    born = models.DateField(verbose_name='Дата рождения')
    description = models.TextField(verbose_name='Биографи')