#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
import  datetime
import  get_min_route 

#c = "curl 'https://www.pokemongomap.info/includes/it55nmsq9.php' -H 'cookie: __cfduid=dfbf5d8335890faa8edbb1efd2f9536aa1523713363; announcementnews11=1; _ga=GA1.2.87903181.1523713375; mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0[##split##]1[##split##]1[##split##]0; PHPSESSID=27s6lvf0c2t2svhuhfa93n7bd4; alertmsg1=1; _gid=GA1.2.1513626770.1524378641; __atuvc=1%7C15%2C0%7C16%2C2%7C17; __atuvs=5adc3389f0fc21cc000; _gat=1; latlngzoom=14[##split##]24.81265088541597[##split##]120.9889554258667' -H 'origin: https://www.pokemongomap.info' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: */*' -H 'referer: https://www.pokemongomap.info/location/24,812651/120,988955/14' -H 'authority: www.pokemongomap.info' -H 'x-requested-with: XMLHttpRequest' --data 'fromlat=24.801120081286108&tolat=24.8241806167653&fromlng=120.94934456313479&tolng=121.02856628859865&fpoke=1&fgym=1&farm=0&nests=0&raids=0&sponsor=0' --compressed" 

#o = os.popen( c ).read()
o = open( 'data' ).read()
a = json.loads(o) 

print a.keys()

l = []
for p in a.keys():
    print p, a[p]['rgqaca']
    c = "curl 'https://www.pokemongomap.info/includes/locdata.php' -H 'cookie: __cfduid=dfbf5d8335890faa8edbb1efd2f9536aa1523713363; announcementnews11=1; _ga=GA1.2.87903181.1523713375; mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0[##split##]1[##split##]1[##split##]0; PHPSESSID=27s6lvf0c2t2svhuhfa93n7bd4; alertmsg1=1; _gid=GA1.2.1513626770.1524378641; __atuvc=1%7C15%2C0%7C16%2C2%7C17; __atuvs=5adc3389f0fc21cc000; latlngzoom=14[##split##]24.810002011802776[##split##]120.9889554258667; _gat=1' -H 'origin: https://www.pokemongomap.info' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'referer: https://www.pokemongomap.info/location/24,810002/120,988955/14' -H 'authority: www.pokemongomap.info' -H 'x-requested-with: XMLHttpRequest' --data 'mid="+p+"' --compressed"
    o = os.popen( c ).read()
    print o
    try:
        j = json.loads(o) 
    except ValueError:
        print 'ERROR: Skip'
        continue
    print j['markerlat'], j['markerlng']
    l.append( ( float(j['markerlat']), float(j['markerlng']) ) )
    time.sleep( 3 )

o = get_min_route.get_route( l )
with open( 'route', 'w' ) as w:
    for p in o:
        w.write( '%f,%f\n' % l[p] )
