#!/usr/bin/python3
"""
project: WayBackNews
SE & Hacker: Ikary Ryann
website: https://www.dirkk.tech
"""


def gettimestamp(cdxdata=[]):
    """Get information for archive site"""

    if cdxdata == []:
        return []

    precision = []
    for sublist in cdxdata:
        urlkey = sublist[0]
        timestamp = sublist[1]
        original = sublist[2]
        mimetype = sublist[3]
        statuscode = sublist[4]
        digest = sublist[5]
        length = sublist[6]
        precision.append(timestamp)
    return precision
