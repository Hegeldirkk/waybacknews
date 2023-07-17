#!/usr/bin/python3
"""
project: WayBackNews
SE & Hacker: Ikary Ryann
website: https://www.dirkk.tech
"""


import os


#class CustomOpener:
#    def __init__(self, file_dir):
#        self.file_dir = file_dir

#def opener(path, flags, file_dir):
#    return os.open(path, flags, dir_fd=file_dir)

def download(text, title):
    """download html page"""

    if len(text) == 0:
        print("Contenu vide")
        exit(0)

    #file_dir = os.open('htmlfile', os.O_RDONLY)
    #path = 'htmlfile'
    #opener = os.open(path, os.O_RDONLY, dir_fd=file_dir)
    name = "download" + title + ".html"
    with open("htmlfile/"+name, "w", encoding="utf-8") as f:
        f.write('{}'.format(text))
        print("fichier enregistrer dans le repertoire htmlfile",)
