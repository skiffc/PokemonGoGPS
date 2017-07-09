#!/usr/bin/env python

import sys
import os
import re
import random

buf = ""
pos = []
speed = 0.0001
circle = 0.0003
for p in open( sys.argv[1] ):
    tpos = []
    for q in p.split(','):
        tpos.append( float(q.strip()) )
    print "*", tpos
    buf += '  <ski lat="%f" lon="%f"></ski>\n' % ( tpos[0], tpos[1] )
    if not pos:
        pos = tpos
    while True: 
        dis2 = ( tpos[0] - pos[0] ) * ( tpos[0] - pos[0] ) + ( tpos[1] - pos[1] ) * ( tpos[1] - pos[1] )
        print dis2
        if dis2 < circle * circle: 
            break
        r = max( random.random(), 0.3 )
        pos[0] += r * ( tpos[0] - pos[0] ) * speed / abs( tpos[0] - pos[0] )  
        pos[1] += r * ( tpos[1] - pos[1] ) * speed / abs( tpos[1] - pos[1] )
        print pos
        buf += '<wpt lat="%f" lon="%f"></wpt>\n' % ( pos[0], pos[1] )

with open( sys.argv[1] + '.gpx', 'w' ) as w:
    w.write( '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<gpx version="1.1" creator="Xcode">\n''' )
    w.write( buf )
    w.write( '</gpx>\n' )
