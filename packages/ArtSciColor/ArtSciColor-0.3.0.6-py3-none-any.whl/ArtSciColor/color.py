#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html

from colour import Color
from numpy import interp
from matplotlib.colors import LogNorm, PowerNorm, SymLogNorm
from matplotlib.colors import ColorConverter, LinearSegmentedColormap

def addHexOpacity(colors, alpha='1A'):
    return [c+alpha for c in colors]


def replaceHexOpacity(colors, alpha='FF'):
    return [i[:-2]+alpha for i in colors]


def generateAlphaColorMapFromColor(color, minAlpha=0, maxAlpha=1):
    """Creates a linear cmap that runs from transparent to full opacity of the provided color.

    Args:
        color (hex string or rgb tuple): Color for cmap
        minAlpha (float): Minimum transparency
        maxAlpha (float): Maximum opacity

    Returns:
        cmap: Matplotlib colormap
    """
    if (type(color) is str):
        color = list(Color(color).rgb)
    alphaMap = LinearSegmentedColormap.from_list(
        'alphaMap', 
        [
            (0, 0, 0, minAlpha), 
            (color[0], color[1], color[2], maxAlpha)
        ]
    )
    return alphaMap

def colorPaletteFromHexList(clist):
    """Takes a list of colors in hex-form and generates a matplotlib-compatible
    cmap function.

    Args:
        clist (list of hex colors): List of colors to be used in the color palette in linear form.

    Returns:
        cmap: LinearSegmentedColormap function for color maps.
    """    
    c = ColorConverter().to_rgb
    clrs = [c(i) for i in clist]
    rvb = LinearSegmentedColormap.from_list("hexMap", clrs)
    return rvb


###############################################################################
# Generate cmap normalizing functions
###############################################################################
def normLinear(vmin=0, vmax=1):
    """Generates a linear interpolation function for cmaps (range 0 to 1) in the
    vmin to vmax range.

    Args:
        vmin (float): Minimum possible input value.
        vmax (float): Maximum possible input value.

    Returns:
        function: Normalizing function to be evaluated.
    """    
    linInterp = lambda x: interp(x, [vmin, vmax], [0, 1], left=None)
    return linInterp

def evalNormColor(
        x, cmap,  
        normFun=SymLogNorm(1, vmin=0, vmax=10),
    ):
    """Evaluates a cmap on the x value given a normalizing function to scale 
    this input value.

    Args:
        x (float): Value to evaluate on.
        cmap (colormap): Matplotlib-compatible colormap.
        normFun (function): Normalizing function (normLinear, LogNorm, PowerNorm, SymLogNorm, etc).

    Returns:
        color: Evaluated color on the cmap.
    """    
    scaledValue = normFun(x)
    color = cmap(scaledValue)
    return color