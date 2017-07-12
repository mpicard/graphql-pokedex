from django_filters import FilterSet, OrderingFilter

from pokemon.models import Pokemon, PokemonType


class PokemonFilter(FilterSet):
    order_by = OrderingFilter(fields=[('name', 'name')])

    class Meta:
        fields = {'name': ['icontains']}
        model = Pokemon


class PokemonTypeFilter(FilterSet):
    order_by = OrderingFilter(fields=[('name', 'name')])

    class Meta:
        fields = {'name': ['icontains']}
        model = PokemonType
