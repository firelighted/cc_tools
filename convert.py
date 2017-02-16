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
    # TEST INCREMENTALLY
    # WRITE, TEST make_cc_data_from_json FIRST - DO TITLE, ETC. BEFORE OPTIONAL FIELDS

    #thatdata = make_cc_data_from_dat('data\pfgd_test.dat') # DAT VERSION

    # with open('pfgd_test.txt', 'w') as f:
    #     f.write(str(thatdata))
    # f.close()

    json_data = cc_json_utils.make_cc_data_from_json(input_json_filename) # DO FIRST
    with BufferedWriter(FileIO(output_dat_file, "wb")) as writer:
        cc_dat_utils.write_cc_data_to_dat(json_data, writer)
    # double check step:
    dat_data = cc_dat_utils.make_cc_data_from_dat(output_dat_file)
    print("Finished!")
convert()