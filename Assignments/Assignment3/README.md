COMP 3532 Assignment 3

Student Name: Honghai Mei **(Luke)**

Student Number: A01075487

To Execute this program

Goto pokedex.py, and run it in command line with parameters:

Here's test script for you

ECHO write to screen
python pokedex.py --inputfile input_ability.txt ability
python pokedex.py --inputdata 2 move
python pokedex.py --inputdata 2 pokemon
python pokedex.py --inputfile input_move.txt move

ECHO write to file
python pokedex.py --inputfile input_move.txt --output output_move.txt move
python pokedex.py --inputfile input_ability.txt --output output_ability.txt ability
python pokedex.py --inputfile input_pokemon.txt --output output.txt pokemon

ECHO write to file expanded
python pokedex.py --inputfile input_pokemon.txt --output output_pokemon_expand.txt pokemon --expanded

ECHO error
python pokedex.py --inputfile input_error.txt --output output_error.txt move

UML of Poke Retriever: