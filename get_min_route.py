#!/usr/bin/env python

import sys
import os
import re
import random
from math import asin, atan, cos, exp, log, pi, sin, sqrt, tan

#def distance( a, b ):
#    return sqrt( ( a[0] - b[0] ) ** 2 + ( a[1] - b[1] ) ** 2 )
def distance( a, b ):
    lat1, lon1 = a
    lat2, lon2 = b
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * \
        cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) * 1000


def get_route( points ):
    dis = {}
    min_dis = 1000
    min_pos = None
    
    for p in range( len(points) ):
        for q in range( p + 1, len(points) ):
            #print p, q
            d = distance( points[p], points[q] )
            if d < min_dis:
                min_dis = d
                min_pos = p
            if p in dis:
                dis[p][q] = d
            else:
                dis[p] = { q: d }
    
            if q in dis:
                dis[q][p] = d
            else:
                dis[q] = { p : d }
    
    print min_pos, min_dis
    route = [ min_pos ] 
    while len(route) < len(points):
        #print dis[route[-1]]
        np = min( dis[route[-1]], key= lambda x: ( x in route, dis[route[-1]][x] ) )
        print points[route[-1]], '->', points[np]
        route.append( np )
    return route
if __name__ == "__main__":
    points = []
    for p in open( 'dgpx' ):
        s = p.strip().split()
        pos = s[3].split(',')
        pos = ( float(pos[0]), float(pos[1]) )
        print pos
        points.append( pos )
        get_route( points )

