import graphene
from graphene_django.types import DjangoObjectType

from pokemon import models, filters


class PokemonTypeNode(DjangoObjectType):

    class Meta:
        model = models.PokemonType
        # interfaces = [relay.Node]

class PokemonNode(DjangoObjectType):
    image_url = graphene.String()
    types = graphene.List(PokemonTypeNode)

    @graphene.resolve_only_args
    def resolve_types(self):
        return self.types.all()

    class Meta:
        model = models.Pokemon
        # interfaces = [relay.Node]


class Query(graphene.AbstractType):
    all_pokemon = graphene.List(PokemonNode)
    all_types = graphene.List(PokemonTypeNode)

    def resolve_all_pokemon(self, args, context, info):
        return models.Pokemon.objects.all()

    def resolve_all_types(self, args, context, info):
        return models.PokemonType.objects.all()
