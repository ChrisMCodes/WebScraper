#!/usr/bin/env python3
# As a fun challenge, I want to adapt this script to alert me
# to new jobs that mention webscraping and Python.
# This will be my project for the week (if I don't get
# sidetracked with something more exciting)


import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            print("\n", url)


scrape = Scraper("https://news.google.com")
scrape.scrape()
