from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=32)
    types = models.ManyToManyField('PokemonType', blank=True)

    def __str__(self):
        return self.name.title()


class PokemonType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name.title()