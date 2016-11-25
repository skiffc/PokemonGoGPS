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
buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0], center[1] ) 
buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] + 0.00012341, center[1] ) 
buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0], center[1] + 0.00000923 ) 
buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] + 0.000010232, center[1] ) 
buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] + 0.000004, center[1] + 0.000005 ) 
buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] - 0.000014, center[1] + 0.000004 ) 
buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] - 0.000004, center[1] + 0.000003 ) 
buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( center[0] + 0.000004, center[1] + 0.000002 ) 

buf += '</gpx>'
open( 'gps.gpx', 'w' ).write( buf )
os.system( 'osascript update_gps.scpt' )
