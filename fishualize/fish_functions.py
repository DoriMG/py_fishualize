import pandas as pd
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.pyplot as plt

global df

def get_data():
    '''Loads the fish color dataset.'''
    global df
    df = pd.read_csv('data\\fishcolors.csv')

def fish_palettes():
    '''Returns all the fish options.

    Returns:
    ndarray: strings of all fish species in dataset
    '''
    global df
    all_options = df.option.unique()
    return all_options

def hex_to_rgba(hex, alpha = 1.):
    '''Transforms hex color into rgb representation.

    Source: https://gist.github.com/matthewkremer/3295567

    Parameters:
    hex (string): String containing hex color (including #)
    alpha (float, 0-1): Alpha value of color

    Returns:
    tuple: (r,g,b,a) values for color
    '''
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple([int(hex[i:i+hlen//3], 16)/255 for i in range(0, hlen, hlen//3)] + [alpha])

def make_cdict(color_array, alpha = 1., direction = 1):
    '''Make the color dictionary required to make LinearSegmentedColormap.

    Parameters:
    color_array (ndarray): array with the rgba values of all colors in the
                           pallette
    alpha (float, 0-1): alpha value for the colors
    direction (int, 1 or -1): direction of the color map

    Returns:
    dict: dictionary containing arrays of transitions for red, green, blue and
          alpha.

    '''
    cdict_names = ['red', 'green', 'blue', 'alpha']
    cdict = {}

    colors = np.array([hex_to_rgba(cl, alpha) for cl in color_array])
    for cl in range(4):
        new_col = np.concatenate((np.expand_dims(np.linspace(0,1,colors.shape[0]),axis=1),
                                  np.expand_dims(colors[::direction,cl], axis=1),
                                  np.expand_dims(colors[::direction,cl], axis=1)), axis=1)

        cdict[cdict_names[cl]] = new_col
    return cdict

def fish(n_colors = 8, option = 'Hypsypops_rubicundus',  alpha = 1., direction = 1):
    '''Generate the colormap for a given fish species

    Parameters:
    n_colors (int): number of colors in the colormap
    option (string): name of the fish
    '''
    if isinstance(option, int):
        if option < 0:
            raise Exception('Your option has to be a positive number')
        elif option >= len(fish_palettes()):
            raise Exception('The number you chose exceeds the number of fish in the database')
        else:
            option = fish_palettes()[option]
    elif isinstance(option, str):
            if not option in fish_palettes():
                raise Exception('That fish is not in the database, please check your spelling and try again')
    else:
        raise Exception('The type of your option needs to be either an integer or a string')
    if not abs(direction) == 1:
        raise Exception('Direction has to be either -1 (backward) or 1 (forward)')

    color_array = np.array(df[df.option == option].hex)
    cdict = make_cdict(color_array, alpha, direction)
    newcmp = LinearSegmentedColormap('testCmap', segmentdata=cdict, N=n_colors)
    return newcmp
