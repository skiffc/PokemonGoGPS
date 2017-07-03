#!/usr/bin/env python

import sys
import os
import re
import random
from math import pi, asin, atan, cos, exp, log, pi, sin, sqrt, tan

for p in open( 'gps.gpx' ):
    if 'wpt' in p:
        center = p.split('"')
        center = [ float( center[1] ), float( center[3] ) ]
        break


move_to = ''.join( sys.argv[1:] ).split(',')
move_to = [ float(move_to[0]), float(move_to[1]) ]

print center, '->', move_to
cnt = 0

buf = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<gpx version="1.1" creator="Xcode"> 
'''

while abs( center[0] - move_to[0] ) > 0.00005 or abs( center[1] - move_to[1] ) > 0.00005:
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0], center[1] ) 
    cnt += 1

    if move_to[0] > center[0]:
        center[0] += max( 0.00001, random.random() * 0.00005 )
    else:
        center[0] -= max( 0.00001, random.random() * 0.00005 )

    if move_to[1] > center[1]:
        center[1] += max( 0.00001, random.random() * 0.00005 )
    else:
        center[1] -= max( 0.00001, random.random() * 0.00005 )

print cnt, 'moves'
for i in range(1000):
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0], center[1] ) 
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] + 0.00012341, center[1] ) 
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0], center[1] + 0.00000923 ) 
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] + 0.000010232, center[1] ) 
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] + 0.000004, center[1] + 0.000005 ) 
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] - 0.000014, center[1] + 0.000004 ) 
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] - 0.000004, center[1] + 0.000003 ) 
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] + 0.000004, center[1] + 0.000002 ) 

buf += '</gpx>'
open( 'move.gpx', 'w' ).write( buf )
os.system( 'new_gps.py %f,%f' % ( center[0], center[1] ) )
os.system( 'osascript update_move.scpt' )
