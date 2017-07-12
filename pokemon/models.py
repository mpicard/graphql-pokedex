from django.conf import settings
from django.db import models
from django.contrib.staticfiles.templatetags.staticfiles import static


class Pokemon(models.Model):
    name = models.CharField(max_length=32)
    types = models.ManyToManyField('PokemonType', blank=True)

    def __str__(self):
        return self.name.title()

    @property
    def image_url(self):
        return static(f'img/pokemon/{self.id}.png')

class PokemonType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name.title()