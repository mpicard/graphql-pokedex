import os
import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from pokemon.models import PokemonType, Pokemon


class Command(BaseCommand):
    help = 'Import CSV data'
    can_import_settings = True

    path_data = os.path.join(settings.BASE_DIR, 'data')

    def get_path(self, filename):
        return os.path.join(self.path_data, filename)

    def handle(self, *args, **options):
        # Types
        # =====
        pokemon_type_instances = []
        with open(self.get_path('types.csv')) as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for r in reader:
                pokemon_type_instances.append(self.create_pokemon_type(r))
        # PokemonType.objects.bulk_create(pokemon_type_instances)

        # Pokemons
        # ========
        pokemon_instances = []
        with open(self.get_path('pokemons.csv')) as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for r in reader:
                pokemon_instances.append(self.create_pokemon(r))
        # Pokemon.objects.bulk_create(pokemon_instances)

        # Pokemon-Types
        # =============
        with open(self.get_path('pokemon_types.csv')) as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for r in reader:
                try:
                    pokemon = Pokemon.objects.get(id=r['pokemon_id'])
                    pokemon_type = PokemonType.objects.get(id=r['type_id'])
                except (Pokemon.DoesNotExist, PokemonType.DoesNotExist):
                    pass

    def create_pokemon(self, data):
        return Pokemon(name=data['identifier'])

    def create_pokemon_type(self, data):
        return PokemonType(name=data['identifier'])

