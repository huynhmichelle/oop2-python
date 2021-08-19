from pokeretriever.PokedexObject import PokedexObject


class Pokemon(PokedexObject):
    """
    Represents a Pokemon.
    """
    def __init__(self, height, weight, stats, types, abilities, moves, **kwargs):
        """
        Initialize Pokemon details
        :param height: an int
        :param weight: an int
        :param stats: list of tuples or list of Stats items
        :param types: list of string
        :param abilities: list of string or list of Ability
        :param moves: list of tuples or list of Move
        :param kwargs: other dictionary key value pairs
        """
        super().__init__(**kwargs)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    def __str__(self):
        """
        Return Pokemon details in a formatted string.
        :return: a formatted string with Pokemon details
        """
        stats = "\n".join([stat.__str__().strip("'") for stat in self._stats])
        abilities = "\n".join([ability.__str__() for ability in self._abilities])
        moves = "\n".join([move.__str__() for move in self._moves])
        types = ", ".join(self._types)
        return super().__str__() + f"Height: {self._height} decimetres\n" \
                                   f"Weight: {self._weight} hectograms\n" \
                                   f"Types: {types}\n\n" \
                                   f"Stats:\n" \
                                   f"------\n" \
                                   f"{stats}\n\n" \
                                   f"Abilities:\n" \
                                   f"------\n" \
                                   f"{abilities}\n\n" \
                                   f"Moves:\n" \
                                   f"------\n" \
                                   f"{moves}\n"
