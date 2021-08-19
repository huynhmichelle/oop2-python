import abc

from pokeretriever.Ability import Ability
from pokeretriever.Move import Move
from pokeretriever.Pokemon import Pokemon
from pokeretriever.Stats import Stats


class BaseFactory(abc.ABC):
    """
    Abstract factory class for Pokedex Objects.
    """
    @abc.abstractmethod
    def create_item(self, json_dict):
        """
        Create a Pokedex Object.
        :param json_dict: a dictionary with necessary values to initialize a Pokedex Object
        :return: a PokedexObject
        """
        pass


class AbilityFactory(BaseFactory):
    """
    Factory class for Ability objects.
    """
    def create_item(self, ability_dict):
        """
        Return an Ability object.
        :param ability_dict: dictionary with key-value pairs necessary to initialize an Ability object
        :return: Ability
        """
        generation = ability_dict["generation"]["name"]
        if ability_dict["effect_entries"]:
            effect = ability_dict["effect_entries"][1]["effect"]
            short_effect = ability_dict["effect_entries"][1]["short_effect"]
        else:
            effect = "N/A"
            short_effect = "N/A"
        pokemon = []
        for item in ability_dict["pokemon"]:
            pokemon.append(item["pokemon"]["name"])
        name = ability_dict["name"]
        ability_id = ability_dict["id"]
        return Ability(generation, effect, short_effect, pokemon, name, ability_id)


class MoveFactory(BaseFactory):
    """
    Factory class for Move objects.
    """
    def create_item(self, move_dict):
        """
        Return a Move object.
        :param move_dict: dictionary with key-value pairs necessary to initialize a Move object
        :return: Move
        """
        generation = move_dict["generation"]["name"]
        accuracy = move_dict["accuracy"]
        pp = move_dict["pp"]
        power = move_dict["power"]
        move_type = move_dict["type"]["name"]
        damage_class = move_dict["damage_class"]["name"]
        if move_dict["effect_entries"]:
            short_effect = move_dict["effect_entries"][0]["short_effect"]
        else:
            short_effect = "N/A"
        name = move_dict["name"]
        move_id = move_dict["id"]
        return Move(generation, accuracy, pp, power, move_type, damage_class, short_effect, name, move_id)


class PokemonFactory(BaseFactory):
    """
    Factory class for Pokemon objects.
    """
    def create_item(self, pokemon_info):
        """
        Return a Pokemon object.
        :param pokemon_info: dictionary with key-value pairs necessary to initialize a Move object
        :return: Pokemon
        """
        pokemon_info["types"] = [pokemon_type["type"]["name"] for pokemon_type in pokemon_info["types"]]

        if type(pokemon_info["stats"][0]) is not Stats:
            pokemon_info["stats"] = [(stat["stat"]["name"], stat["base_stat"]) for stat in pokemon_info["stats"]]
            pokemon_info["abilities"] = [ability["ability"]["name"] for ability in pokemon_info["abilities"]]
            pokemon_info["moves"] = [("Move name: " + move["move"]["name"], "Level acquired: " + str(move["version_group_details"][0]["level_learned_at"])) for move in pokemon_info["moves"]]

        return Pokemon(**pokemon_info)


class StatsFactory(BaseFactory):
    """
    Factory class for Stats objects.
    """
    def create_item(self, stats_info):
        """
        Return a Stats object.
        :param stats_info: dictionary necessary to initialize a Stats object
        :return: Stats
        """
        return Stats(**stats_info)
