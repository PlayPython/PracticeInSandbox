#!/usr/bin/env python
import re

try:
    input_dir = raw_input("Please enter the directory:")
    input_file_name = raw_input("Please enter the file name and file type:")
    input_file = input_dir + '/' + input_file_name
    files = open(input_file, 'r')
except IOError:
    print "file input wrong.Please input as format:/Users/ran.li/Downloads"
else:
    file_content = files.read()
    # question here : pattern is not so accurate :
    #  eg: alre@#ady  alre  ady
    pattern = r'[A-Za-z]+'
    p = re.compile(pattern)
    print "The file has {0} words".format(len(p.findall(file_content)))
    files.close()
