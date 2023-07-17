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
import asyncio
gettimestamp = __import__('gettimetamps').gettimestamp
download = __import__('download').download


class Waybacknews:
    """represent News back"""

    def __init__(self, load=0, site='https://www.dirkk.tech'):
        """Initialize load
        Args:
            load (int): counter for loading
        """
        print(Fore.WHITE + 'Enter the target domain (like this' + Fore.RED +' "dirkk.tech"' + Fore.WHITE + ') : ')
        domain = input(Fore.CYAN + '==> ')

        if domain.isdigit():
            print(Fore.RED + 'Please enter a domain: dirkk.tech')
            exit(0)

        self.load = load
        self.site = domain
        Waybacknews.checkDomain(self)

    def checkDomain(self):
        """check Availability of enter site"""

        #get last archive site
        arUrl = "https://archive.org/wayback/available?url=" + self.site
        resp = requests.get(arUrl)

        if resp.status_code in range(400, 600):
            print(Fore.RED + 'Some problems')
            exit(-1)

        archive = resp.json()
        date = archive['archived_snapshots']['closest']['timestamp']
        datetime = date[:4] + '/' +date[4:-8] + '/' + date[6:-6]
        hours = date[8:-4] + ':' + date[10:-2] + ':' + date[12:]

        print(("{} {} {}").format(Fore.WHITE + '[-- Status Code --]: ', Fore.GREEN, resp.status_code))
        sleep(0.5)
        print(("{} {} {}").format(Fore.WHITE + '[-- Available Last Version --]: ', Fore.GREEN, archive['archived_snapshots']['closest']['available']))
        sleep(0.5)
        print(("{} {} {}").format(Fore.WHITE + '[-- Code Status last Version --]: ', Fore.GREEN, archive['archived_snapshots']['closest']['status']))
        sleep(0.5)
        print(("{} {} {}").format(Fore.WHITE + '[-- Date Last Version --]: ', Fore.GREEN, datetime))
        sleep(0.5)
        print(("{} {} {}").format(Fore.WHITE + '[-- Hours Last Version --]: ', Fore.GREEN, hours))

        sleep(1)
        print(("{}").format(Fore.YELLOW + 'Would you like to have older versions of this site ? yes or no',))
        query = input(Fore.CYAN + '==> ')

        if query == 'yes' or query == 'y' or query == '':
            Waybacknews.showOlder(self.site)
        else:
            print(("{}").format(Fore.YELLOW + 'What Content are you looking for in one of the older versions of this site?',))
            content = input(Fore.CYAN + '==> ')
            findcontent = str(content)
            asyncio.run(Waybacknews.findContent(self, findcontent))

    def showOlder(site):
        """display another older version in this site"""
        precision = []
        idtest = 0
        print(("{}").format(Fore.YELLOW + 'How much content do you want to have ?',))
        nb = input(Fore.CYAN + '==> ')
        cdxSite = "http://web.archive.org/cdx/search/cdx?url=" + site + "&output=json&limit=" + nb
        getOlder = requests.get(cdxSite)
        value = getOlder.json()
        print(Fore.WHITE + '[------ Year of which the contents are available --------]')
        sleep(0.5)
        print(Fore.WHITE + '[------ Here are the ' + nb + ' older contents of this site: ' + Fore.MAGENTA + site + Fore.WHITE + '  --------]')
        for sublist in value:
            idtest += 1
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
            print(Fore.WHITE + '[==============> Nº ' + str(idtest - 1) + '  Date: ' + Fore.MAGENTA + datetime + '  ' + hours)
            sleep(2)

        #print(precision)
        sleep(3)
        print(("{}").format(Fore.YELLOW + 'choose the number of the content to use:',))
        chxdate = int(input(Fore.CYAN + '==> (2)'))
        paragraph_length = 0
        while paragraph_length == 0:
            sleep(0.3)
            print(("{}").format(Fore.YELLOW + 'Waiting......',))
            resp = requests.get("http://web.archive.org/web/" + precision[int(chxdate)]  + "/http://www." + site)
            soup = BeautifulSoup(resp.text, 'html.parser')
            contentpage = soup.find_all('p')
            link = soup.find_all('a')
            paragraph_length = len(contentpage)
            print(("{}").format(Fore.MAGENTA + str(paragraph_length) + Fore.WHITE + ' paragraphs found on this page !',))
            if paragraph_length == 0:
                print(("{}").format(Fore.YELLOW + 'would you like to choose another date ? yes or no',))
                response = str(input(Fore.CYAN + '==> '))
                if response == 'yes':
                    sleep(3)
                    print(("{}").format(Fore.YELLOW + 'choose the number of the content to use:',))
                    chxdate = int(input(Fore.CYAN + '==> (2)'))

        for paragraph in range(0, paragraph_length):
            print(contentpage[paragraph].text.strip())
            sleep(1)
        print(("{}").format(Fore.MAGENTA + str(len(link)) + Fore.WHITE + ' all link in this page',))
        sleep(0.5)
        print(link)
        sleep(1)
        print(("{}").format(Fore.YELLOW + 'would you like download this page ? yes or no',))
        resdownload = str(input(Fore.CYAN + '==> '))

        if resdownload == "yes":
            download(self.site, precision[int(chxdate)])

    async def findContent(self, content):
        """function to find content"""
        #print(self.site)
        page = []
        cdxSite = "http://web.archive.org/cdx/search/cdx?url=" + self.site + "&output=json"
        getAll = requests.get(cdxSite)
        contentTimestamps = gettimestamp(getAll.json())

        for version in contentTimestamps:
            if version != "timestamps":
                res = requests.get("http://web.archive.org/web/" + version  + "/http://www." + self.site)
                soup = BeautifulSoup(res.text, 'html.parser')
                html_doc = res.content
                if str(content) in html_doc.decode('utf-8'):
                    page.append(version)
                    print("[=====> Total found:" + str(len(page)))
                    #print(soup.get_text())
        print(Fore.WHITE + '[------ Content found in ' + Fore.MAGENTA + str(len(page)) + Fore.WHITE + ' old page  --------]')
        print(("{}").format(Fore.YELLOW + 'would you like download this page ? yes or no',))
        resCttDownload = str(input(Fore.CYAN + '==> '))

        i = 0
        if resCttDownload == "yes":
            for i in range(0, len(page)):
                download(self.site, page[i])

if __name__ == '__main__':
    Waybacknews()
