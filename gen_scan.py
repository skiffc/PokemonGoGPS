#!/usr/bin/env python

import sys
import os
import re
import random
from math import pi, asin, atan, cos, exp, log, pi, sin, sqrt, tan

center = ''.join( sys.argv[1:] ).split(',')
center = [ float(center[0]), float(center[1]) ]

buf = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<gpx version="1.1" creator="Xcode"> 
'''

l = []
l.append( center )
l.append( center )
l.append( [ center[0] + 0.0001, center[1] + 0.0003 ] )
l.append( [ center[0] - 0.0001, center[1] + 0.0006 ] )
res = 128
for i in range( 0, res ):
    l.append( [ center[0] + sin(2*pi*i/res)*0.0009, center[1] + cos(2*pi*i/res)*0.0009 ] )
l.append( [ center[0] - 0.0001, center[1] + 0.0012 ] )
l.append( [ center[0] + 0.0001, center[1] + 0.0015 ] )
res = 256
for i in range( 0, res ):
    l.append( [ center[0] + sin(2*pi*i/res)*0.0018, center[1] + cos(2*pi*i/res)*0.0018 ] )

for p in l: 
    buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( p[0], p[1] )

l.append( [ center[0] + 0.0001, center[1] + 0.0014 ] )
l.append( [ center[0] - 0.0001, center[1] + 0.0010 ] )
l.append( [ center[0] + 0.0001, center[1] + 0.0007 ] )
l.append( [ center[0] - 0.0001, center[1] + 0.0003 ] )

buf += '</gpx>'
open( 'scan.gpx', 'w' ).write( buf )
