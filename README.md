# fishualize

Color Palettes Based on Fish Species
This is the python version of the R package made by [Nina Schiettekatte](https://github.com/nschiett), Simon Brandl and Jordan Casey. Find the R package on their [GitHub page](https://github.com/nschiett/fishualize). All credit to them for the dataset and the idea behind the package!

## Installation
You can find the package on pip:
~~~~
pip install fishualize
~~~~

## Usage

To get all the possible fish options, run `fish_palettes()`

To create a colormap, use the `fish` function. Several parameters are available:
* n_colors: the number of colors you want the colormap to have.
* option: the fish you want the pallette of (can be either int or string).
* alpha: the alpha of the entire pallette.
* direction: the direction of the colormap (either forward (1) or reverse (-1)).
