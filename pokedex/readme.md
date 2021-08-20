# Object-Oriented Pokedex

## Overview
A Pokedex is a useful device for trainers in the 
Pokemon universe that want to seek out information about
various Pokemon.

In this assignment, we implemented a Pokedex prototype
in Python, using asyncio and aiohttp for GET HTTP requests.
We queried from [PokeAPI](https://pokeapi.co/) to get
information about the Pokemon universe.

Our UML class diagram for this assignment can be found 
[here](https://github.com/huynhmichelle/oop2-python/pokedex/blob/master/a3_uml_class_diagram.png).

## How the program works
In this program, users can query information about a Pokemon,
an ability, or a move. Users can do this through the 
command line. 
### Commands
The following is general syntax for running the program and entering 
a query:

`python pokedex.py {"pokemon" | "ability" | "move"} {--inputfile 
"filename.txt" | --inputdata "name or id"} [--expanded] [--output "filename.txt"]`

A breakdown of the syntax is provided below.
#### python pokedex.py
Depending on your system, you may want to enter `python` or `python3`. The Python 
module that we want to execute is `pokedex.py`.
#### {"pokemon" | "ability" | "move"} 
One of the three values must be provided. This will indicate the mode that we want to
run. This means if we want to retrieve details of a certain Pokemon, we will enter 
`pokemon`. If we want details about an ability, we will enter `ability`. If we want 
details about a move, we will enter `move`.
#### {--inputfile "filename.txt" | --inputdata "name or id"}
Users can pass in an input text file with the names or ids of the Pokemon, ability,
move that are desired. If so, the flag `--inputfile` should be entered with the file
path to the text file. If providing just the name or id directly, it can be entered 
after entering the flag `--inputdata`. `--inputfile` and `inputdata` are mutually
exclusive.
#### [--expanded]
This is an optional argument specifically for the `pokemon` mode. If this flag is 
entered in the command line, additional information about a Pokemon's abilities, moves,
and stats will be provided in the output.
#### [--output "filename.txt"] 
This is an optional argument as well. If this flag is provided, alongside a file name 
with a .txt extension, the query result's output will be entered in that file. If 
this flag is not provided, then the result will be displayed in the console.

### Mode details
This section will provide an overview of what attributes are returned according to the
mode provided in the query.
#### Pokemon
Entering this mode in the command line will retrieve information about a Pokemon, 
specifically the following attributes:
* **Name**
* **ID**
* **Height (in decimetres)**
* **Weight (in hectograms)**
* **Stats**: by default (meaning if the `--expanded` flag is not added when running
  the program), only the stat name and its base value will be stored and outputted. 
  If the `--expanded` flag is added, then more detailed stat information will be provided
  through querying the corresponding stat URL.
* **Types**: the type of the Pokemon (e.g. grass, fire, flying)
* **Abilities**: similar to stats, by default only the ability name is stored. If the 
`--expanded` flag is added, then more detailed information about the ability will be 
  provided.
* **Moves**: similar to Stats and Abilities regarding the `--expanded` flag. By default,
only the move name and the level is acquired is provided.
#### Stats
More information about stats is provided only when querying Pokemon in expanded mode,
particularly:
* **Name**
* **ID**
* **Is battle only**
#### Ability
An ability is an effect that certain Pokemon can enable. The Pokedex program can 
query ability information when running in the ability mode, specifically details about:
* **Name**
* **ID**
* **Generation**
* **Effect**
* **Effect (short)**: shorter version description of the effect
* **Pokemon**: a list of Pokemon that can have this ability
#### Move
A move is an attack/action that Pokemon can execute. Different Pokemon have and can
acquire different types of moves. The program can query move information when running 
in the move mode, specifically details about:
* **Name**
* **ID**
* **Generation**
* **Accuracy**
* **PP** (power points, the number of times this move can be used)
* **Power**
* **Type**
* **Damage class**
* **Effect (short)**


## Example
pokedex.py file on the root directory of the project holds main driver.
In order to execute the program you must either 1) navigate to where the pokedex.py 
file is, or 2) know the path to the pokedex.py

Below is the example of how to execute the program to output pikachu information on console
```cmd
python {pokedex.py or path to pokedex.py} pokemon --inputdata pikachu 
```

You can combine different fields according to the commands in above section to query 
for more complex information such as multiple different objects of the same mode, and output
into a file.

Below is an example of a more complex command. It will request for following ten entries in the 
input_pokemon.txt with expand flag on and output the result to output_pokemon.py file

input_pokemon.txt:
```txt
1
2
3
4
5
6
7
8
9
10
```
command:
```cmd
python {pokedex.py or path to pokedex.py} pokemon --inputfile {path to input_pokemon.txt} --output output_pokemon.txt --expand
```
## Error/Edge Case
### Case sensitivity
commands and input data are case-sensitive. This includes id/name in input file

```cmd
python pokedex.py pokemon -inputdata Pikachu // ouput error message
python pokedex.py pokemon -inputdata PIKACHU // output error message
python pokedex.py pokemon -inputdata pikachu // output correct Pokemon data
```

### Input File Extension
input file must be a text file with '.txt' extension

```cmd
python pokedex.py pokemon -inputfile input.doc // Program will throw UnicodeDecodeError
python pokedex.py pokemon -inputfile input.txt // executes successfully
```

### Input File Format
There must be only one entry in a single line in input file for the program to read the input correctly.
Make sure our input.txt doesn't consist of an empty line, especially at the end of the file as it is easy to miss.

valid example of input.txt:
```txt
1
2
3
```

invalid examples of input.txt:
```txt
1 2
3
```
```txt
1,2,3
```
```txt
1
2
3

```


### Invalid Modes
The only modes supported by this program are: pokemon, ability, and move. 
Other modes offered by pokemon api are not recognized by our program

```cmd
python pokedex.py berry --inputdata 1

>> usage: pokedex.py [-h] (--inputfile INPUTFILE | --inputdata INPUTDATA) [--expanded] [--output OUTPUT] {pokemon,ability,move}
>> pokedex.py: error: argument mode: invalid choice: 'poke' (choose from 'pokemon', 'ability', 'move')
```

### API Limit
According to the Pokémon api documentation, up to 300 requests are allowed per resource per IP address. So a single IP address 
can call the bulbasaur resource 300 times a day. Not 300 requests across the entire dataset.

Having tested this limit, it seemed more than 300 requests for the same resource with the same IP address
can be made; however, it is not a guarantee and users should be aware of the limit.
