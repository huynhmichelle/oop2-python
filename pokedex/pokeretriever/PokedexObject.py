class PokedexObject:
    """
    parent class for pokedexObject.
    """
    def __init__(self, name, id, **kwargs):
        """
        Initialized PokedexObject.
        :param name: string
        :param id: int
        :param kwargs: other dictionary key pair values
        """
        self._name = name
        self._id = id

    def __str__(self):
        """
        Return PokedexObject details in a formatted string.
        :return: a formatted string with PokedexObject details
        """
        return f"Name: {self._name}\n" \
               f"ID: {self._id}\n"
