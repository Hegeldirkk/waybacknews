#!/usr/bin/python3
"""
project: WayBackNews
SE & Hacker: Ikary Ryann
website: https://www.dirkk.tech
"""


import os
import requests
from colorama import Fore


def download(site, title):
    """download html page"""

    res = requests.get("http://web.archive.org/web/" + title  + "/http://www." + site)
    text = res.text
    if len(text) == 0:
        print("Contenu vide")
        exit(0)

    datetime = title[:4] + '-' +title[4:-8] + '-' + title[6:-6]
    hours = title[8:-4] + ':' + title[10:-2] + ':' + title[12:]

    name = "download" + title + ".html"
    with open("htmlfile/"+name, "w", encoding="utf-8") as f:
        f.write('{}'.format(text))
        print("Version du : " + Fore.Magenta + datetime + " " + hours + Fore.WHITE + "enregistrer dans le repertoire htmlfile: " + name)
