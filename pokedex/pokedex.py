import argparse
import asyncio
import logging
import time

from pokeretriever.PokeObjectRequest import PokeObjectRequest


class Request:
    """
    Represents a Request to get Pokemon-related data from an API.
    """
    def __init__(self):
        """
        Initialize Request details.
        """
        self.mode = None
        self.is_input_file = None
        self.input_content = None
        self.expanded = None
        self.output = None

    def __str__(self):
        return f"Mode: {self.mode}\n" \
               f"is_input_file: {self.is_input_file}\n" \
               f"input_content: {self.input_content}\n" \
               f"expanded: {self.expanded}\n" \
               f"output: {self.output}"


def setup_request_commandline():
    """
    Uses argparse module to accept arguments provided through command
    line. Provided arguments are parsed and passed into a Request object.
    :return: a Request with provided arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("mode",
                        choices=("pokemon", "ability", "move"))

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.required = True
    input_group.add_argument("--inputfile")
    input_group.add_argument("--inputdata")

    parser.add_argument("--expanded",
                        action="store_true")

    parser.add_argument("--output")

    try:
        args = parser.parse_args()
        request = Request()
        request.mode = args.mode
        request.is_input_file = True if args.inputdata is None else False
        request.input_content = args.inputfile if args.inputdata is None else args.inputdata
        request.expanded = args.expanded
        request.output = args.output
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Pokedex:
    """
    Represents a Pokedex, executing the request and outputting the
    requested details.
    """
    def execute_request(self, request):
        """
        Executes the request and passes result to a print output method.
        :param request: a Request
        :return: None
        """
        request.input_content = self.read_file(request.input_content) if request.is_input_file else [
            request.input_content]
        poke_request = PokeObjectRequest(request.mode, request.input_content, request.expanded)
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(poke_request.execute())
        self.print_output(result, request.output)

    @staticmethod
    def read_file(file_path):
        """
        Reads a file from a file path and splits data from the file into
        a list.
        :param file_path: a str
        :return: data as a list of strings
        """
        with open(file_path, mode="r", encoding="utf-8") as f:
            data = f.read()
        return data.split("\n")

    @staticmethod
    def print_output(pokedex_items, file_path):
        """
        Print requested Pokedex items.
        :param pokedex_items: list of PokedexObject items
        :param file_path: a str
        :return: None
        """
        timestamp = time.strftime("%d/%m/%Y %H:%M")
        if file_path is None:
            print(f"Timestamp: {timestamp}")
            print(f"Number of requests: {len(pokedex_items)}")
            for item in pokedex_items:
                print(item.__str__())
            return
        with open(file_path, mode="w", encoding="utf-8") as f:
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"Number of requests: {len(pokedex_items)}\n")
            for item in pokedex_items:
                f.write(item.__str__())
                f.write("\n")


def main(request):
    """
    Drives the program.
    :param request: a Request
    :return: None
    """
    logging.basicConfig(level=logging.DEBUG)
    pokedex = Pokedex()
    pokedex.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
