#! /usr/bin/env python

import sys

functor_name = sys.argv[1]
functor_path = '.'
if len(sys.argv) == 3:
    functor_path = sys.argv[2]
functor_file_name = functor_path + '/' + functor_name + '.oz'
# functor = open(functor_file_name, 'w')
header = """
/*-------------------------------------------------------------------------
 *
 * %s
 *
 *  <Short Description>
 *
 * LICENSE
 *
 *    Beernet is released under the Beerware License (see file LICENSE) 
 * 
 * IDENTIFICATION 
 *
 *    Author: $Author$
 *
 *    Last change: $Revision$ $Author$
 *
 *    $Date$
 *
 * NOTES
 *      
 *  <If any>
 *
 *-------------------------------------------------------------------------
 */""" % functor_file_name
header = header.lstrip()
print header

