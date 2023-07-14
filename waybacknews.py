#!/usr/bin/python3
"""
project: WayBackNews
SE & Hacker: Ikary Ryann
website: https://www.dirkk.tech
"""


import requests
from colorama import Fore, Back, Style
from time import sleep
from bs4 import BeautifulSoup


class Waybacknews:
    """represent News back"""

    def __init__(self, load=0, site='https://www.dirkk.tech'):
        """Initialize load
        Args:
            load (int): counter for loading
        """
        self.load = load
        self.site = site

    def checkDomain():
        """check Availability of enter site"""
        print(Fore.WHITE + 'Saisissez l\'url:')
        url = input(Fore.CYAN + '==> ')

        if url.isdigit():
            print(Fore.RED + 'svp veuillez saisir une url: https://www.dirkk.tech')

        arUrl = "https://archive.org/wayback/available?url=" + url
        resp = requests.get(arUrl)

        if resp.status_code in range(400, 600):
            print(Fore.RED + 'Some problems')

        print(("{} {} {}").format(Fore.WHITE + '[-- Status Code --]: ', Fore.GREEN, resp.status_code))

        sleep(0.5)
        archive = resp.json()
        #print(archive)
        print(("{} {} {}").format(Fore.WHITE + '[-- Available Last Version --]: ', Fore.GREEN, archive['archived_snapshots']['closest']['available']))
        sleep(0.5)
        print(("{} {} {}").format(Fore.WHITE + '[-- Code Status last Version --]: ', Fore.GREEN, archive['archived_snapshots']['closest']['status']))
        sleep(0.5)
        date = archive['archived_snapshots']['closest']['timestamp']
        datetime = date[:4] + '/' +date[4:-8] + '/' + date[6:-6]
        print(("{} {} {}").format(Fore.WHITE + '[-- Date Last Version --]: ', Fore.GREEN, datetime))
        sleep(0.5)
        hours = date[8:-4] + ':' + date[10:-2] + ':' + date[12:]
        print(("{} {} {}").format(Fore.WHITE + '[-- Hours Last Version --]: ', Fore.GREEN, hours))

        sleep(1)
        print(("{}").format(Fore.YELLOW + 'Souhaitez-vous avoir les anciens version de ce site ?',))
        query = input(Fore.CYAN + '==> ')

        if query == 'yes':
            Waybacknews.showOlder(url)
        else:
            exit(0)

    def showOlder(site):
        """display another older version in this site"""
        precision = []
        print(("{}").format(Fore.YELLOW + 'Combien de contenu souhaitez vous avoir ?',))
        nb = input(Fore.CYAN + '==> ')
        cdxSite = "http://web.archive.org/cdx/search/cdx?url=" + site + "&output=json&limit=" + nb
        getOlder = requests.get(cdxSite)
        value = getOlder.json()
        print(Fore.WHITE + '[------ Année dont les contenus sont disponibles --------]')
        sleep(0.5)
        print(Fore.WHITE + '[------ Voici les ' + nb + ' plus vieux contenus de ce site: ' + Fore.MAGENTA + site + Fore.WHITE + '  --------]')
        for sublist in value:
            urlkey = sublist[0]
            timestamp = sublist[1]
            original = sublist[2]
            mimetype = sublist[3]
            statuscode = sublist[4]
            digest = sublist[5]
            length = sublist[6]

            #date time
            precision.append(timestamp)
            datetime = timestamp[:4] + '-' +timestamp[4:-8] + '-' + timestamp[6:-6]
            hours = timestamp[8:-4] + ':' + timestamp[10:-2] + ':' + timestamp[12:]
            print(Fore.WHITE + '[==============> Date: ' + Fore.MAGENTA + datetime + '  ' + hours)
            sleep(2)

        #print(precision)
        sleep(3)
        print(("{}").format(Fore.YELLOW + 'Quel Contenu recherchez vous dans ces versions ?',))
        content = input(Fore.CYAN + '==> ')
        print(("{}").format(Fore.YELLOW + 'A la quelle des dates ?',))
        chxdate = int(input(Fore.CYAN + '==> '))
        sleep(0.3)
        print(("{}").format(Fore.YELLOW + 'Waiting......',))
        resp = requests.get("http://web.archive.org/web/" + precision[int(chxdate) + 1]  + "/http://www." + site)
        soup = BeautifulSoup(resp.text, 'html.parser')
        contentpage = soup.find_all('p')
        paragraph_length = len(contentpage)
        print(("{}").format(Fore.MAGENTA + str(paragraph_length) + Fore.WHITE + ' paragraphes trouvé sur cette page',))

        for paragraph in range(0, paragraph_length):
            print(contentpage[paragraph])
            sleep(1)

if __name__ == '__main__':
    Waybacknews.checkDomain()
