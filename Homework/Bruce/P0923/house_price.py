#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re


class HousePrice(object):
    counter = 0
    m = {}

    def __init__(self):
        pass

    def run(self, base_url):
        for page in range(1, 10):
            url = "{0}{1}".format(base_url, page)
            self.get_detail(url)

        counter = 0
        for name in self.m:
            counter += 1
            print str(counter) + " " + name + " " + self.m[name]

    def get_detail(self, url):
        page = self.get_html(url)
        info_list = re.findall(r'(.*)onclick="shoucangProcess(.*)', page)

        for info in info_list:
            house_info = info[1].split(');"')[0]
            house = house_info.split(',')
            house_name = self.remove_quote(house[1])
            house_price = self.remove_quote(house[4])
            house_unit = self.remove_quote(house[5])

            house_type = house_unit.split('/')[0]
            if house_type == u'元' and house_price != u'价格待定':
                print str(self.counter) + " " + house_name + " " + house_price
                self.m[house_name] = house_price

    @staticmethod
    def get_html(url):
        r = requests.get(url)
        r.encoding = 'gb2312'
        response = r.text

        return response

    @staticmethod
    def remove_quote(string):
        if len(string) > 1 and "'" in string:
            return string.split("'")[1]
        else:
            return string


if __name__ == '__main__':
    hp = HousePrice()
    hp.run("http://newhouse.cd.fang.com/house/s/gaoxinqu/b9")
