#!/usr/bin/python3
"""
project: WayBackNews
SE & Hacker: Ikary Ryann
website: https://www.dirkk.tech
"""


import os
import requests


def download(site, title):
    """download html page"""

    res = requests.get("http://web.archive.org/web/" + title  + "/http://www." + site)
    text = res.text
    if len(text) == 0:
        print("Contenu vide")
        exit(0)

    name = "download" + title + ".html"
    with open("htmlfile/"+name, "w", encoding="utf-8") as f:
        f.write('{}'.format(text))
        print("fichier enregistrer dans le repertoire htmlfile",)
