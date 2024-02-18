#!/usr/bin/python
"""
Python module for various plotting helpers to display
generalized susceptibility matrices.
"""
import numpy as np
import scipy as sp
import matplotlib as mpl

def cdict_cw(points = 10_001):
    """
    returns:
        colormap dictionary inspired by Patrick Chalupa: the colormap
        is a sequential blue-white-red map and enhances the visibility
        of small deviations from the central value
    """
    half = points//2
    cp = np.linspace(0,1,points,endpoint=True)

    green = np.zeros(points)
    blue = np.zeros(points)
    red = np.zeros(points)

    green[:half]= 1-(1-2.*cp[:half])**(1/2)
    green[half]= 1
    green[half+1:]= 1-(1-2.*cp[:half][::-1])**(1/2)
    red[half]= 1
    red[half+1:]= 1-cp[1:half+1]
    blue[half]= 1
    blue[:half]= 1-cp[1:half+1][::-1]


    Gn = np.column_stack((cp[:],green[:],green[:]))
    Rd = np.column_stack((cp[:],red[:],red[:]))
    Bu = np.column_stack((cp[:],blue[:],blue[:]))

    return  {'green':  Gn,
             'blue':  Bu,
             'red':  Rd}


def cdict_gr(points = 10_001):
    """
    returns:
        colormap dictionary: the colormap is a sequential 
        green-brown-red map and enhances the visibility
        of small deviations from the central value
    """
    half = points//2
    cp = np.linspace(0,1,points,endpoint=True)

    green = np.zeros(points)
    blue = np.zeros(points)
    red = np.zeros(points)

    green[:half]= (1-2.*cp[:half])**(1/2)
    green[half]=green[half-1]/2
    red[half+1:]= 0.25+(np.array(1.-2*cp[:half])[::-1])**(1/2)
    red[half]= red[half+1]/2
    blue[np.where(red>1)]= red[np.where(red>1)]-1.
    red[np.where(red>1)] = 1.

    Gn = np.column_stack((cp[:],green[:],green[:]))
    Rd = np.column_stack((cp[:],red[:],red[:]))
    Bu = np.column_stack((cp[:],blue[:],blue[:]))

    return  {'green':  Gn,
             'blue':  Bu,
             'red':  Rd}

def cdict_gy(points = 10_001):
    """
    returns:
        colormap dictionary: the colormap is a sequential 
        green-black-yellow map and enhances the visibility
        of small deviations from the central value
    """
    half = points//2
    cp = np.linspace(0,1,points)

    green = np.zeros(points)
    blue = np.zeros(points)
    red = np.zeros(points)

    green[:half]= (1-2.*cp[:half])**(1/7)
    green[half+1:]= 0.8*(1-2.*cp[:half][::-1])**(1/7)
    green[half] = 0.
    red[half]= 0.
    red[half+1:]= 0.25+(np.array(1.-2*cp[:half])[::-1])**(1/7)
    blue[np.where(red>1)]= red[np.where(red>1)]-1.
    red[np.where(red>1)] = 1.

    Gn = np.column_stack((cp[:],green[:],green[:]))
    Rd = np.column_stack((cp[:],red[:],red[:]))
    Bu = np.column_stack((cp[:],blue[:],blue[:]))


    return  {'green':  Gn,
             'blue':  Bu,
             'red':  Rd}

def cmap_gy(points = 6_001):
    """
    returns:
        sequential green-black-yellow colormap with enhanced visibility
        of small deviations from the central value
    """
    return mpl.colors.LinearSegmentedColormap('reitner_gy',
                                              segmentdata = cdict_gy(points)
                                              ,N=points).reversed()

def cmap_gr(points = 6_001):
    """
    returns:
        sequential green-brown-red colormap with enhanced visibility
        of small deviations from the central value
    """
    return mpl.colors.LinearSegmentedColormap('reitner_gr',
                                              segmentdata = cdict_gr(points)
                                              ,N=points).reversed()
def cmap_nw(points = 6_001):
    """
    returns:
        sequential blue-white-red colormap with enhanced visibility
        of small deviations from the central value
        Inspired by Patrick Chalupa
    """
    return mpl.colors.LinearSegmentedColormap('chalupa_white',
                                              segmentdata = cdict_cw(points)
                                              ,N=points).reversed()
def cmap_w(points = 10_000):
    # -------------------------------------
    # colormap inspired by Patrick Chalupa
    # -------------------------------------
    cdict_white = {'blue':  [[0.0, 0.6, 0.6],
                       [0.499, 1.0, 1.0],
                       #[0.5, 0.0, 0.0],
                       [0.5, 1.0, 1.0],
                       [0.501, 0.0, 0.0],
                       [1.0, 0., 0.]],
             'green': [[0.0, 0.0, 0.0],
                       [0.02631578947368421, 7.673360394717657e-06, 7.673360394717657e-06],
                       [0.05263157894736842, 0.00012277376631548252, 0.00012277376631548252],
                       [0.07894736842105263, 0.0006215421919721302, 0.0006215421919721302],
                       [0.10526315789473684, 0.0019643802610477203, 0.0019643802610477203],
                       [0.13157894736842105, 0.004795850246698536, 0.004795850246698536],
                       [0.15789473684210525, 0.009944675071554084, 0.009944675071554084],
                       [0.18421052631578946, 0.018423738307717093, 0.018423738307717093],
                       [0.21052631578947367, 0.031430084176763524, 0.031430084176763524],
                       [0.23684210526315788, 0.050344917549742546, 0.050344917549742546],
                       [0.2631578947368421, 0.07673360394717657, 0.07673360394717657],
                       [0.2894736842105263, 0.11234566953906126, 0.11234566953906126],
                       [0.3157894736842105, 0.15911480114486534, 0.15911480114486534],
                       [0.3421052631578947, 0.21915884623353094, 0.21915884623353094],
                       [0.3684210526315789, 0.2947798129234735, 0.2947798129234735],
                       [0.39473684210526316, 0.3884638699825815, 0.3884638699825815],
                       [0.42105263157894735, 0.5028813468282164, 0.5028813468282164],
                       [0.4473684210526315, 0.6408867335272133, 0.6408867335272133],
                       [0.47368421052631576, 0.8055186807958807, 0.8055186807958807],
                       [0.499, 1.0, 1.0],
                       #[0.5, 0.0, 0.0],
                       [0.5, 1.0, 1.0],
                       [0.501, 1.0, 1.0],
                       [0.5263157894736843, 0.8055186807958807, 0.8055186807958807],
                       [0.5526315789473685, 0.6408867335272133, 0.6408867335272133],
                       [0.5789473684210527, 0.5028813468282164, 0.5028813468282164],
                       [0.6052631578947368, 0.3884638699825815, 0.3884638699825815],
                       [0.631578947368421, 0.2947798129234735, 0.2947798129234735],
                       [0.6578947368421053, 0.21915884623353094, 0.21915884623353094],
                       [0.6842105263157895, 0.15911480114486534, 0.15911480114486534],
                       [0.7105263157894737, 0.11234566953906126, 0.11234566953906126],
                       [0.736842105263158, 0.07673360394717657, 0.07673360394717657],
                       [0.7631578947368421, 0.050344917549742546, 0.050344917549742546],
                       [0.7894736842105263, 0.031430084176763524, 0.031430084176763524],
                       [0.8157894736842105, 0.018423738307717093, 0.018423738307717093],
                       [0.8421052631578947, 0.009944675071554084, 0.009944675071554084],
                       [0.868421052631579, 0.004795850246698536, 0.004795850246698536],
                       [0.8947368421052632, 0.0019643802610477203, 0.0019643802610477203],
                       [0.9210526315789473, 0.0006215421919721302, 0.0006215421919721302],
                       [0.9473684210526316, 0.00012277376631548252, 0.00012277376631548252],
                       [0.9736842105263158, 7.673360394717657e-06, 7.673360394717657e-06],
                       [1.0, 0.0, 0.0]],
             'red':   [[0.0, 0., 0.],
                       [0.499, 0.0, 0.0],
                       [0.5, 1.0, 1.0],
                       #[0.5, 0.0, 0.0],
                       [0.501, 1.0, 1.0],
                       [1.0, 0.6, 0.6]]}

    return mpl.colors.LinearSegmentedColormap('chalupa_white',segmentdata = cdict_white,N=points)

# ---------------------------------------
# normalize colormap around zero value
# ---------------------------------------
class norm(mpl.colors.Normalize):
    """
    class to normalize matplotlib colorbar around midpoint from stackoverflow

    attributes:
        matrix (float, array) array to calculate colormap norm
        midpoint (float, optional) midpoint
        clip (bool, optional)

    """
    def __init__(self, matrix, midpoint=0, clip=False):
        # normalize only real part
        M= np.real(matrix)
        vmin = np.amin(M)
        vmax = np.amax(M)
        self.midpoint = midpoint
        mpl.colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        """
        args:
            value (float)
            clip (optional)
        
        returns:
            masked array for colorbar normalization
        """
        if self.vmax == 0:
            normalized_min = 0
        else:
            normalized_min = max(0, 1 / 2 * (1 - abs((self.midpoint - self.vmin) \
                                                     / (self.midpoint - self.vmax))))
        if self.vmin == 0:
            normalized_max = 1
        else:
            normalized_max = min(1, 1 / 2 * (1 + abs((self.vmax - self.midpoint) \
                                                     / (self.midpoint - self.vmin))))
        normalized_mid = 0.5
        x = [self.vmin, self.midpoint, self.vmax] 
        y = [normalized_min, normalized_mid, normalized_max]
        return np.ma.masked_array(np.interp(value, x, y))
