import asyncio

import aiohttp

from pokeretriever.Factory import StatsFactory, PokemonFactory, AbilityFactory, MoveFactory


class PokeObjectRequest:
    """
    Represents a Pokemon Object Request.
    """
    FACTORY_MAP = {"pokemon": PokemonFactory(),
                   "ability": AbilityFactory(),
                   "move": MoveFactory(),
                   "stat": StatsFactory()}

    def __init__(self, mode, values, expanded=False):
        """
        Initialize PokeObjectRequest details.
        :param mode: a str
        :param values: list of str
        :param expanded: a bool
        """
        self._mode = mode
        self._values = values
        self._expanded = expanded
        self._factory = self.FACTORY_MAP[mode]
        self._base_url = "http://pokeapi.co/api/v2/{}/{}"

    async def get_data(self, url, mode, session):
        """
        Executes GET request and return requested information as a
        PokedexObject.
        :param url: a str
        :param mode: a str representing the mode e.g. ability, pokemon, move
        :param session: a HTTP session
        :return: a type of PokedexObject
        """
        expandable_mode = "pokemon"
        expandable_map = {"ability": "abilities",
                          "move": "moves",
                          "stat": "stats"}
        response = await session.request(method="GET", url=url)
        try:
            json_dict = await response.json()
        except aiohttp.ClientError:
            return "An error occurred. Skipping this request.\n"
        if self._expanded and mode == expandable_mode:
            for sub_mode, directory in expandable_map.items():
                sub_json = json_dict
                sub_json = sub_json[directory]
                sub_url_list = [obj[sub_mode]["url"] for obj in sub_json]
                tasks = [self.get_data(sub_url, sub_mode, session) for sub_url in sub_url_list]
                json_dict[directory] = await asyncio.gather(*tasks)
        return PokeObjectRequest.FACTORY_MAP[mode].create_item(json_dict)

    async def execute(self):
        """
        Run multiple async tasks.
        :return: list of dict containing responses from GET request
        """
        async with aiohttp.ClientSession() as session:
            tasks = [self.get_data(self._base_url.format(self._mode, val), self._mode, session) for val in self._values]
            responses = await asyncio.gather(*tasks)
        return responses
