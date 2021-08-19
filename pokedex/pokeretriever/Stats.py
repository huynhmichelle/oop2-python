from pokeretriever.PokedexObject import PokedexObject


class Stats(PokedexObject):
    """
    Represents a Stats.
    """
    def __init__(self, is_battle_only, **kwargs):
        """
        Initialize Pokemon details
        :param is_battle_only: boolean
        :param kwargs: other key value pairs
        """
        super().__init__(**kwargs)
        self._is_battle_only = is_battle_only

    def __str__(self):
        """
        Return Stats details in a formatted string.
        :return: a formatted string with Stats details
        """
        return super().__str__() + f"Is_Battle_Only: {self._is_battle_only}\n"
