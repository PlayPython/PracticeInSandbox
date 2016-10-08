#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


class HousePrice(object):
    m = {}
    counter = 0
    home_url = "http://esf.cd.fang.com/house-a0136"

    def __init__(self):
        pass

    def run(self, base_url):
        total_page = self.get_page(self.home_url)

        for page in range(1, total_page):
            url = "{0}{1}".format(base_url, page)
            print "Loading {0}/{1}...".format(page, total_page)
            self.get_detail(url)

        counter = 0
        for name in self.m:
            counter += 1
            print str(counter) + " " + name + " " + self.m[name]

    def get_detail(self, url):
        page = self.get_html(url)
        soup = BeautifulSoup(page, "html.parser")
        list = soup.find_all('dd', 'info rel floatr')
        for node in list:
            name_html = node.select('p a span')
            price_html = node.find_all('p', 'danjia alignR mt5')

            name = name_html[0].contents[0]
            price = price_html[0].contents[0]
            self.m[name] = price

    @staticmethod
    def get_html(url):
        r = requests.get(url)
        r.encoding = 'gb2312'
        response = r.text

        return response

    def get_page(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        page_html = soup.find_all('span', 'fy_text')
        page_info = page_html[0].contents[0]
        page = int(page_info.split('/')[1])
        return page

    @staticmethod
    def remove_quote(string):
        if len(string) > 1 and "'" in string:
            return string.split("'")[1]
        else:
            return string


if __name__ == '__main__':
    base_url = "http://esf.cd.fang.com/house-a0136/i3"
    hp = HousePrice()
    hp.run(base_url)
