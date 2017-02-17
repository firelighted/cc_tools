import test_data
import sys
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    # Set up GameLibrary instance with Game and Platform instances
    game_library_data = test_data.GameLibrary()
    for game, desc in json_dict.items():
        platf = test_data.Platform(desc['platform'].get('name'), desc['platform'].get('launch year'))
        thegame = test_data.Game(desc['title'], platf, desc['year'])
        game_library_data.add_game(thegame)#Create a new Game object from the json_data by reading
        #  title, year, platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library

    return game_library_data

# Handling command line arguments
#  Note: sys.argv is a list of strings that contains each command line argument
#        The first element in the list is always the name of the python file being run
# Command line format: <input json filename>

default_input_json_file = "data/test_data.json"

if len(sys.argv) == 2:
    input_json_file = sys.argv[1]
    print("Using command line args:", input_json_file)
else:
    print("Unknown command line options. Using default values:", default_input_json_file)
    input_json_file = default_input_json_file

#Load the json data from the input file
with open(input_json_file, 'r') as jsondata:
    json_dict = json.load(jsondata)
game_library_data = make_game_library_from_json(json_dict)

#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
game_library_strings = test_data.print_game_library(game_library_data)
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
print(game_library_strings)