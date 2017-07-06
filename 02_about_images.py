#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:52:28 2017

@author: ivan
"""

import urllib.request
import os
from scipy import misc

#print(os.path.isdir("/home/el"))
#print(os.path.exists("/home/el/myfile.txt"))




_have_pil = True
try:
    from scipy.misc.pilutil import imread as _imread
except ImportError:
    _have_pil = False

__all__ = ['imread']

def imread(fname, flatten=False, mode=None):
    if _have_pil:
        return _imread(fname, flatten, mode)
    raise ImportError("Could not import the Python Imaging Library (PIL)"
                      " required to load image files.  Please refer to"
                      " http://pillow.readthedocs.org/en/latest/installation.html"
                      " for installation instructions.")

if _have_pil and _imread.__doc__ is not None:
    imread.__doc__ = _imread.__doc__.replace('name : str', 'fname : str')

#newpath = r'C:\Program Files\arbitrary' 
#if not os.path.exists(newpath):
#    os.makedirs(newpath)
    
def create_folder(path = './nueva_carpeta'):
    ''' Create a folder
    
    Keyword arguments:
    path -- String   - ./neuva_carpeta
    '''
    if not os.path.exists(path):
        os.makedirs(path)

def download_image(url, destination, image_name, extension = '.jpg'):
    ''' download an image from an url
    
    Keyword arguments:
    url         : String
    destination : String
    image_name  : String
    extension   : String   - default: .jpg
    '''
    urllib.request.urlretrieve(url, destination + '/' + image_name + extension)
    
def download_product_images(product_dict, folder_name = 'product_images'):
    ''' download al the product images from a product_dict, where product_list 
    is a dictionary with the structure of product_id: image_url
    
    Keyword arguments:
    product_dict : dict String/Integer : String
    folder_name  : String  - default: product_images
    '''
    create_folder('./' + folder_name)
#    print('Creanda carpeta')
    for product_id, url in product_dict.items():
        download_image(url, folder_name, product_id)
#        print('Descarga completa', product_id)
        
def load_image(directory, name, mode = 'bw', extension = '.jpg'):
    ''' Returns a numpy array with the info about the pixels in the image
    
    Keyword arguments:
        directory -- String
        name      -- String
        mode      -- String : color / bw
        extension -- String
    '''
    if mode == 'color':
        arr = imread(directory + '/' + name + extension, flatten = False)
    elif mode == 'bw':
        arr = imread(directory + '/' + name + extension, flatten = True)
    return arr
    