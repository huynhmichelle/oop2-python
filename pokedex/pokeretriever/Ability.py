from pokeretriever.PokedexObject import PokedexObject


class Ability(PokedexObject):
    """
    Represents a Ability.
    """
    def __init__(self, generation, effect, short_effect, pokemon, *args):
        """
        Initialize Ability details.
        :param generation: a str
        :param effect: a str
        :param short_effect: a str
        :param pokemon: a list of strings representing Pokemon names
        :param args: Ability name, ID
        """
        super().__init__(*args)
        self._generation = generation
        self._effect = effect
        self._short_effect = short_effect
        self._pokemon = pokemon

    def __str__(self):
        """
        Return Ability details in a formatted string.
        :return: a formatted string with Ability details
        """
        pokemon = ", ".join(self._pokemon)
        return super().__str__() + f"Generation: {self._generation}\n" \
                                   f"Effect: {self._effect}\n" \
                                   f"Effect (short): {self._short_effect}\n" \
                                   f"Pokemon that can have this ability: {pokemon}\n\n"
