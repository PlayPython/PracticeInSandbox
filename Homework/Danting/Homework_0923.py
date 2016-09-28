#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import enchant


def wordFilter(path):
    if os.path.isfile(path) == False:
        print("Input is not a file")
    file = open(path)
    count = 0

    # Four kind dictionary
    # en_GB: British English
    # en_US: American English
    # de_DE: German
    # fr_FR: French
    dictionary = enchant.Dict("en_US")

    for line in file.readlines():
        words = line.split()
        for word in words:
            # print(word)
            # print("######")
            word = word.strip(',')
            # print(word)
            if word.isalpha():
                # print(word)
                if dictionary.check(word):
                    count += 1
                    # print(word)
                else:
                    print("{0} is not an English word!".format(word))
    print("word_number::{0}".format(count))


if __name__ == '__main__':
    # path = "/Users/danting.deng/python_study/work.txt"
    # "/Users/danting.deng/python_study/work.txt"
    path = raw_input("Please input file:")
    wordFilter(path)
