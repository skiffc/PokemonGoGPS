#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
from math import asin, atan, cos, exp, log, pi, sin, sqrt, tan
import  datetime

pid = json.load( open( 'pokemon.id' ) )
rank = json.load( open( 'pokemon.rank' ) )
skill = json.load( open( 'pokemon.skill' ) )


#pos = ( 25.03535440009973, 121.57869271090999 ) 
if len(sys.argv) > 1:
    center = ''.join( sys.argv[1:] ).split(',')
    center = [ float(center[0]), float(center[1]) ]
else:
    for p in open( 'gps.gpx' ):
        if 'wpt' in p:
            center = p.split('"')
            center = ( float( center[1] ), float( center[3] ) )
            break

def scan( pos, center=[25,121] ):
    pokemons = pokemons_from_pkget( pos )
    for p in pokemons:
        attr = p[5].split('^')
        found = False
        if attr[5] == '':
            attr[5] = 0

        if p[1] in ( 'Dragonite', 'Snorlax', 'Lapras' ) and float(attr[5]) > 60: 
            found = True
        elif p[1] in ( 'Dratini', 'Dragonair' ) and float(attr[5]) >= 96:
            found = True
        elif ( p[1], skill[attr[3]], skill[attr[4]] ) in [ ( 'Dragonite', 'Dragon Breathe', 'Dragon Claw' ), ( 'Lapras', 'Frost Breathe', 'Blizzard' ), ( 'Snorlax', 'Zen Headbutt', 'Body Slam' ) ]:
            found = True
        elif ( p[1], skill[attr[4]] ) in [ ( 'Dragonite', 'Dragon Claw' ), ( 'Dragonite', 'Dragon Pulse' ), ( 'Snorlax', 'Body Slam' ), ( 'Lapras', 'Blizzard' ) ]:
            found = True
        elif ( p[1], skill[attr[4]] ) in [ ( 'Machamp', 'Cross Chop' ), ( 'Golem', 'Stone Edge' ), ( 'Kabutops', 'Stone Edge' ), ( 'Rhydon', 'Earthquake' ), ( 'Rhydon', 'Stone Edge' ) ]:
            found = True
        elif p[1] in ( 'Omastar', 'Chansey' ):
            found = True

        if found:
            print p[1], "%f,%f" % ( p[2], p[3] ), "%.2fkm" % distance( center[0], center[1], p[2], p[3] ), datetime.datetime.fromtimestamp(p[4]), attr[:3], "%s+%s" % ( skill[attr[3]], skill[attr[4]] )

def pokemons_from_pkget( pos, zoom = 2 ):
    #d1 = ( 24.83529197421961 - 24.81503814442042 ) / zoom
    #d2 = ( 121.05197309619075 - 120.99395155078064 ) / zoom
    d1 = ( 24.818055833105845 - 24.777539228397693 ) / zoom
    d2 = ( 121.0192108154297 - 120.9804153442383 ) / zoom

    #cd1 = ( 24.8321372685217 - 24.811882922832897 ) / zoom
    #cd2 = ( 121.03952764636165 - 120.98150610095149 ) / zoom
    cd1 = ( 24.81447220571424 - 24.77395443006801 ) / zoom
    cd2 = ( 121.01303100585939 - 120.97423553466798 ) /zoom


    c = "curl 'https://pkget.com/fp.ashx?a=%f&b=%f&c=%f&d=%f&e=1_1&f=fJwfBKujfRZ2AKkEbHJzqIJzEeEfjSsLYAJaF9YH3djsS7z13yKB%%2BCqAbQUGCtQ3&g=4NqROlwqrT%%2Fl7SuJ820NSelW2rN9MkoITbxrNay6leo%%3D&h=&j=765' -H 'Cookie: ASP.NET_SessionId=4313y42kxovkxkclg4m4s1ue; __gads=ID=af258e6421716de8:T=1499504590:S=ALNI_MaKvNSE7KrDe58kpl789QZBygvy-w; pkgetcomL=1; pkgetcomGen=1; ga=ga=1.1.222588955.1419666884; pkll=24.8032720%%2C120.960845; _ga=GA1.2.1157477300.1498827654; _gid=GA1.2.801311312.1500209470; _gat=1; pkllg=24.8202288%%2C121.00793619999997; pkgetcom=lat0=%f&lng0=%f&lat1=%f&lng1=%f' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://pkget.com/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed" % ( pos[0] + d1, pos[1] + d2, pos[0] - d1, pos[1] - d2, pos[0] + cd1, pos[1] + cd2, pos[0] - cd1, pos[1] - cd2 )

    #c = "curl 'https://pkget.com/pkm333.ashx?v1=111&v2=%f&v3=%f&v4=%f&v5=%f&v6=0' -H 'Cookie: ASP.NET_SessionId=t412njlnw0je1yvvwzicu5h4; _ga=GA1.2.810889542.1472951395; _gat=1; pkgetcom=lat0=%f&lng0=%f&lat1=%f&lng1=%f' -H 'Accept-Encoding: gzip, deflate, sdch, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://pkget.com/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed 2>/dev/null" % ( pos[0] + d1, pos[1] + d2, pos[0] - d1, pos[1] - d2, pos[0] + cd1, pos[1] + cd2, pos[0] - cd1, pos[1] - cd2 )
    #print(c)
    o = os.popen( c ).read()

    pokemons = []
    try:
        j = json.loads(o)
        for p in j['fp']:
            #print p
            if 'd2' not in p:
                p['d2'] = pid['%03d' % int(p['d1'])]
            pokemons.append( [ p['d1'], p['d2'], float(p['d4']), float(p['d5']), int(p['d3'])/1000, p['d9'] ] ) 
    except:
        pass

    print 'Found:', len(pokemons)
    return pokemons

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * \
        cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) 


for x in range( -2, 3, 1 ):
    for y in range( -2, 3, 1 ):
        pos = [ center[0] + x * 0.04, center[1] + y * 0.04 ]
        print --- x, y, pos
        scan( pos, center=center )
        time.sleep( 3 )


