#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:31:25 2017

@author: ivan
"""

import requests
import json


def coords(location):
    """ Returns the a json-formatted coordinates pair
    the output has the structure:
        {'northeast': {'lat': -, 'lng': -}, 'southwest': {'lat': -, 'lng': -}}
    
    Keyword arguments:
    location -- String with the place to look for
    
    """
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': location}
    r = requests.get(url, params=params)
    results = r.json()['results'][0]['geometry']['bounds']#['northeast']
    return results