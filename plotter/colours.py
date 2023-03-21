import plotter.auxillary as aux

import numpy as np

import importlib
import itertools

def generate_colours(palettes, kind=None):

    if kind == 'single':
        colour_cycle = itertools.cycle(palettes)

    else:
        # Creates a list of all the colours that is passed in the colour_cycles argument. Then makes cyclic iterables of these. 
        colour_collection = []
        for palette in palettes:
            mod = importlib.import_module("palettable.colorbrewer.%s" % palette[0])
            colour = getattr(mod, palette[1]).mpl_colors
            colour_collection = colour_collection + colour

        colour_cycle = itertools.cycle(colour_collection)


    return colour_cycle



def mix_colours(colour1, colour2, options):

    default_options = {
        'number_of_colours': 10,
        'weights': None
    }

    options = aux.update_options(options=options, default_options=default_options)

    if not options['weights']:
        options['weights'] = [x/options['number_of_colours'] for x in range(options['number_of_colours'])]

    colours = []
    for weight in options['weights']:
        colour = []

        for c1, c2 in zip(colour1, colour2):
            colour.append(np.round(((1-weight)*c1 + weight*c2), 5))

        colours.append(colour)


    return colours