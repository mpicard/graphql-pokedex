from graphene import Schema, ObjectType

from pokemon.schema import Query as PokemonQuery


class Query(PokemonQuery,  ObjectType):
    # This class should inherit from multiple app Queries
    # to build a nested, project-wide Schema
    pass


schema = Schema(query=Query)