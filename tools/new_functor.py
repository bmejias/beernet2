#! /usr/bin/env python

import sys
import os

pwd         = os.getcwd()
SRC_PATH    = 'beernet2/src/'
package     = pwd[(pwd.find(SRC_PATH) + len(SRC_PATH)):]

script_full = os.path.realpath(__file__)
script_dir  = script_full[:script_full.rfind('/') + 1]
header_fname= script_dir + "header.txt"
header = open(header_fname, 'r')

functor_name = sys.argv[1]
if functor_name[-3:] != '.oz':
    functor_name += '.oz'
functor_full_name = package + '/' + functor_name
functor_path_name = pwd + '/' + functor_full_name
functor = open(functor_name, 'w')

for line in header:
    new_line = line
    if line.find('__filename__') > 0:
        new_line = line.replace('__filename__', functor_full_name)
    functor.write(new_line)

functor.close()
    

