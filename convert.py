import cc_dat_utils
import cc_json_utils
import sys
from io import FileIO, BufferedWriter

"""
TODO:
 test_json_utils: do make_game_library_from_json:
    find Game object
    fill out Game fields


"""

def convert(input_json_filename='data/sasano_cc1.json', output_dat_file='data/sasano_cc1.dat'):
    """"
    convert:
    This function takes an input json file and converts it to a dat file, which is saved in the
    output_dat_file location.
    """
    json_data = cc_json_utils.make_cc_data_from_json(input_json_filename) # DO FIRST
    cc_dat_utils.write_cc_data_to_dat(json_data, output_dat_file)
    # double check step:
    dat_data = cc_dat_utils.make_cc_data_from_dat(output_dat_file)

convert()