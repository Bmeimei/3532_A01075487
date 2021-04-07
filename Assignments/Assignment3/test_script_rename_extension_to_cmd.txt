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
