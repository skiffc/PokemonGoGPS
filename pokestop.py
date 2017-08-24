#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
import  datetime
import  get_min_route 

c = "curl 'https://www.pokemongomap.info/includes/uy22ewsd1.php' -H 'Cookie: mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0; announcement2=1; __atssc=reddit%3B1; announcementnews=1; PHPSESSID=kd01tlrmfkdtjgtgs62o5fdo61; announcementnews4=1; announcementnews6=1; __atuvc=17%7C30%2C4%7C31%2C9%7C32%2C1%7C33%2C1%7C34; _ga=GA1.2.1811255488.1499521885; _gid=GA1.2.2056522202.1503488353; latlngzoom=14[##split##]25.000138632709938[##split##]121.3139910584167' -H 'Origin: https://www.pokemongomap.info' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: https://www.pokemongomap.info/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'fromlat=24.9803397545244&tolat=25.019934321092585&fromlng=121.27438019568478&tolng=121.35360192114865&fpoke=1&fgym=1&farm=0&nests=0&raids=1' --compressed" 

o = os.popen( c ).read()
a = json.loads(o) 

print a.keys()

l = []
for p in a.keys():
    print p, a[p]['rgqaca']
    c = "curl -s 'https://www.pokemongomap.info/includes/locdata.php' -H 'Cookie: mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0; announcement2=1; __atssc=reddit%3B1; announcementnews=1; PHPSESSID=kd01tlrmfkdtjgtgs62o5fdo61; announcementnews4=1; __atuvc=1%7C27%2C6%7C28%2C8%7C29%2C17%7C30%2C3%7C31; __atuvs=5981b9580122d5d5000; _ga=GA1.2.1811255488.1499521885; _gid=GA1.2.1336496384.1501673817; latlngzoom=16[##split##]24.79043586095946[##split##]121.00303720290218' -H 'Origin: https://www.pokemongomap.info' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://www.pokemongomap.info/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'mid="+p+"' --compressed" 
    o = os.popen( c ).read()
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
