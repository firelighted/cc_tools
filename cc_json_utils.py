"""
Methods for encoding and decoding Chip's Challenge (CC) data to and from binary DAT files
Created for the class Programming for Game Designers
"""
import cc_data
import json

def make_level_from_json(level_dict):
    cc_level = cc_data.CCLevel() #constructor
    cc_level.level_number = level_dict['level_number']
    cc_level.time = level_dict['time']
    cc_level.num_chips = level_dict['chip_number']
    cc_level.upper_layer = level_dict['upper']
    cc_level.lower_layer = level_dict['lower']
    cc_level.optional_fields = make_optional_fields_from_json((level_dict["optional"]))
    return cc_level


def make_cc_data_from_json(json_file):
    data = cc_data.CCDataFile() # class constructor
    with open(json_file, 'r') as jsondata:
        json_dict = json.load(jsondata)
    for game, desc in json_dict.items():
        # platf = test_data.Platform(desc['platform'].get('name'), desc['platform'].get('launch year'))
        # thegame = test_data.Game(desc['title'], platf, desc['year'])
        # game_library_data.add_game(thegame)
        cc_level = make_level_from_json(desc)
        data.add_level(cc_level)
    return data



def make_optional_fields_from_json(json_optional_fields):
    cc_fields = []
    for json_field in json_optional_fields: # iterate through optional_field list
        field_type = json_field["type"] # access key of each field
        if field_type == cc_data.CCMapTitleField.TYPE: # map title
            cc_fields.append(cc_data.CCMapTitleField(json_field["title"]))
        elif field_type == cc_data.CCTrapControlsField.TYPE: # trap_buttons
            trapControlList = []
            for trap in json_field["trap_buttons"]:
                trapControlList.append(cc_data.CCTrapControl(trap[0], trap[1], trap[2], trap[3]))
            cc_fields.append(cc_data.CCTrapControlsField(trapControlList))
        elif field_type == cc_data.CCCloningMachineControlsField.TYPE:  # clone_buttons
            cloneControlList = []
            for trap in json_field["clone_buttons"]:
                cloneControlList.append(cc_data.CCCloningMachineControl(trap[0], trap[1], trap[2], trap[3]))
            cc_field = cc_data.CCCloningMachineControlsField(cloneControlList)
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCEncodedPasswordField.TYPE:  # encoded_password
            cc_fields.append(cc_data.CCEncodedPasswordField(json_field["encoded_password"]))
        elif field_type == cc_data.CCMapHintField.TYPE:  # hint
            cc_fields.append(cc_data.CCMapHintField(json_field["hint"]))
        elif field_type == cc_data.CCMonsterMovementField.TYPE:
            cc_monsters = []
            # EXTRACT COOD FROM json_optional_fields
            for cood in json_field["moving_monsters"]: # iterate thru cood lists
                cc_monsters.append(cc_data.CCCoordinate(cood[0], cood[1]))
            cc_field = cc_data.CCMonsterMovementField(cc_monsters)
            cc_fields.append(cc_field)
        else:
            print("cc_json_utils.py: make_optional_fields_from_json function detected unauthorized field.")
    return cc_fields
