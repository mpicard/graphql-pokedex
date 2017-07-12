from django.contrib import admin
from django.conf import settings

from pokemon.models import Pokemon, PokemonType


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display =  ('id', '__str__', 'img')
    list_filter = ('types',)
    ordering = ('id',)

    def img(self, obj):
        url = f'{settings.STATIC_URL}img/pokemon/{obj.id}.png'
        return f'<img src="{url}" height=40>'

    img.allow_tags = True
    img.__name__ = 'Image'


@admin.register(PokemonType)
class PokemonTypeAdmin(admin.ModelAdmin):
    pass
