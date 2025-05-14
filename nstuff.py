#!/usr/bin/env python3

"""
nstuff.py

Replacement for the now defunct cgi MiniFieldStorage

Parse GET and/or POST data into a dict

With a POST request you can parse
POST data and the url query string. 

"""

import json
import  sys
from os import environ as E
from urllib.parse import parse_qsl

version="0.1.9"

CT="CONTENT_TYPE"
CL= "CONTENT_LENGTH"
QS="QUERY_STRING"

POST="application/x-www-form-urlencoded"


def _prestuff(ndata):
    """
    prestuff parse urlencoded GET and POST data
    into key /value pairs. returned as a dict.
    """
    nparsed = parse_qsl(ndata)
    return {a[0]: a[1] for a in nparsed}


def getstuff():
    """
    getstuff return GET key/value pairs.
    returned as a dict.
    """
    if QS in E:
        ndata = E[QS]
        return _prestuff(ndata)
    return {}


def poststuff():
    """
    poststuff  POST key/value pairs.
    returned as a dict.
    """
    if  CT in E:
        if E[CT] == POST :
            ndata = sys.stdin.buffer.read(int(E[CL])).decode()
            return _prestuff(ndata)
    return {}


def nstuff():
    '''
    nstuff  return GET and/or POST key/value pairs.
    You can do a POST with a QUERY_STRING and
    parse the key/value pairs from the POST data
    and the QUERY_STRING from the URL.
    '''
    stuff={}
    stuff.update(getstuff())
    stuff.update(poststuff())
    return stuff

if __name__ == '__main__':
    formstuff = nstuff()
    print("Content-type: text/Json\n")
    print(json.dumps(formstuff))
