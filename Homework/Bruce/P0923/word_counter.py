#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import enchant
import re


class WordCounter(object):

    def __init__(self, file_name):
        self.file_name = file_name

        if len(self.file_name) < 1:
            print "file name can't be null"
            exit()
        elif not os.path.isfile(self.file_name):
            print "NOT found the file {0}".format(self.file_name)
            exit()

    def run(self):
        counter = 0
        with open(self.file_name, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    words = re.findall(r"[a-zA-Z]+", line)
                    for word in words:
                        if self.is_word(word):
                            counter += 1

        print "The file has {0} words.".format(counter)

    def is_word(self, word):
        dic = enchant.Dict("en_US")
        return dic.check(word)


if __name__ == '__main__':
    file_name = raw_input('Input file name:')

    wc = WordCounter(file_name)
    wc.run()
