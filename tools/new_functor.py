#! /usr/bin/env python

import sys
import os

SRC_PATH    = 'beernet2/src/'

def help_msg(exit_status):
    print "Usage: %s <component_name>" % os.path.basename(sys.argv[0])
    print ""
    print "Note: This command only makes sense within path %s" % SRC_PATH
    sys.exit(exit_status)

if len(sys.argv) != 2:
    print "ERROR: Wrong invocation"
    help_msg(1)

if sys.argv[1] == "help":
    help_msg(0)

pwd     = os.getcwd()
src_pos = pwd.find(SRC_PATH)
if not src_pos > 0:
    print "ERROR: Wrong location. Make sure you are inside %s\n" % SRC_PATH
    help_msg(2)

package = pwd[(src_pos + len(SRC_PATH)):]

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
    

