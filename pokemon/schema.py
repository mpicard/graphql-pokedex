from functools import partial

from graphene import AbstractType, List, relay, resolve_only_args

from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField as FilterField

from pokemon.models import Pokemon, PokemonType
from pokemon.filters import PokemonFilter, PokemonTypeFilter


class PokemonTypeNode(DjangoObjectType):

    class Meta:
        model = PokemonType
        only_fields = ['name']
        # interfaces = [relay.Node]


class PokemonNode(DjangoObjectType):
    types = List(PokemonTypeNode)

    @resolve_only_args
    def resolve_types(self):
        return self.types.all()

    class Meta:
        model = Pokemon
        only_fields = ['name']
        # interfaces = [relay.Node]


class Query(AbstractType):
    all_pokemon = List(PokemonNode)
    all_types = List(PokemonTypeNode)

    def resolve_all_pokemon(self, args, context, info):
        return Pokemon.objects.all()

    def resolve_all_types(self, args, context, info):
        return PokemonType.objects.all()
