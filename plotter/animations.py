import plotter.auxillary as aux

from PIL import Image
import os


def make_animation(paths, options={}):

    default_options = {
        'save_folder': '.',
        'save_filename': 'animation.gif',
        'fps': 5
    }

    options = aux.update_options(options=options, default_options=default_options)


    frames = []
    for path in paths:
        frame = Image.open(path)
        frames.append(frame)

        frames[0].save(os.path.join(options['save_folder'], options['save_filename']), format='GIF', append_images=frames[1:], save_all=True, duration=(1/options['fps'])*1000, loop=0)

    
