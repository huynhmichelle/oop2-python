from pokeretriever.PokedexObject import PokedexObject


class Move(PokedexObject):
    """
    Represents a Move.
    """
    def __init__(self, generation, accuracy, pp, power, type, damage_class, short_effect, *args):
        """
        Initialize Move details.
        :param generation: a str
        :param accuracy: an int
        :param pp: an int
        :param power: an int
        :param type: a str
        :param damage_class: a str
        :param short_effect: a str
        :param args: Move name, ID
        """
        super().__init__(*args)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type
        self._damage_class = damage_class
        self._short_effect = short_effect

    def __str__(self):
        """
        Return Move details in a formatted string.
        :return: a formatted string with Move details
        """
        return super().__str__() + f"Generation: {self._generation}\n" \
                                   f"Accuracy: {self._accuracy}\n" \
                                   f"pp: {self._pp}\n" \
                                   f"Power: {self._power}\n" \
                                   f"Type: {self._type}\n" \
                                   f"Damage class: {self._damage_class}\n" \
                                   f"Effect (short): {self._short_effect}\n\n"
