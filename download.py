#!/usr/bin/python3
"""
project: WayBackNews
SE & Hacker: Ikary Ryann
website: https://www.dirkk.tech
"""


import os


def opener(path, flags):
    return os.open(path, flags, file_dir=file_dir)

def download(text, title):
    """download html page"""

    if len(text) == 0:
        print("Contenu vide")
        exit(0)

    file_dir = os.open('htmlfile', os.O_RDONLY)

    name = "download" + title + ".html"
    with open(name, "w", opener=opener, encoding="utf-8") as f:
        f.write('{}'.format(text))
        print("fichier enregistrer dans le repertoire htmlfile", file=f)

    os.close(file_dir)
