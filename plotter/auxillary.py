import json
import os

def update_options(options, default_options, required_options=None):
    ''' Takes a dictionary of options along with a list of required options and dictionary of default options, and sets all keyval-pairs of options that is not already defined to the default values'''

    for option in default_options.keys():
        if option not in options.keys():
            options[option] = default_options[option]


    return options

def save_options(options, path, ignore=None):
    ''' Saves any options dictionary to a JSON-file in the specified path'''

    options_copy = options.copy()

    if ignore:
        if not isinstance(ignore, list):
            ignore = [ignore]

        for i in ignore:
            options_copy[i] = 'Removed'


    if not os.path.isdir(os.path.dirname(path)):
        if os.path.dirname(path):
            os.makedirs(os.path.dirname(path))


    with open(path, 'w') as f:
        json.dump(options_copy, f, skipkeys=True, indent=4)


def load_options(path):
    ''' Loads JSON-file into a dictionary'''

    with open(path, 'r') as f:
        options = json.load(f)

    return(options)


