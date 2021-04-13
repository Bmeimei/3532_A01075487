# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/3/31 11:11
# File Name:         pokedex.py
from pokeretriever.pokemon_request import PokemonRequest
from pokeretriever.request import Request
from datetime import datetime


def main():
    """
    Executes All Features.
    """
    request = Request.setup_command_line()
    response = PokemonRequest.execute_features(request)
    if request.output == "print":
        print(datetime.now().strftime("%d/%m/%Y %H:%M") + "\n")
        print(f"Number of requests: {len(response)}" + "\n\n")
        for i in response:
            print(i)
    else:
        # Write output to File.
        file_name = request.output
        with open(file_name, "w") as file_object:
            file_object.write(datetime.now().strftime("%d/%m/%Y %H:%M") + "\n")
            file_object.write(f"Number of requests: {len(response)}" + "\n\n")
            for i in response:
                file_object.write(str(i))
                file_object.write("\n")
                file_object.write("------------------")
                file_object.write("\n")
            print("Finished! File is saving at " + file_name)


if __name__ == '__main__':
    main()
