#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
import  datetime
import  get_min_route 

c = "curl 'https://www.pokemongomap.info/includes/uy22ewsd1.php' -H 'Cookie: PHPSESSID=3mcm776vrtlip9kv9556vl1fg7; mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0; announcement2=1; __atssc=reddit%3B1; announcementnews=1; __atuvc=1%7C27%2C6%7C28%2C8%7C29%2C3%7C30; _ga=GA1.2.1811255488.1499521885; _gid=GA1.2.1712956306.1500725650; latlngzoom=16[##split##]25.027201337966527[##split##]121.55954192931209' -H 'Origin: https://www.pokemongomap.info' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: https://www.pokemongomap.info/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'fromlat=25.022855762178878&tolat=25.03154675987945&fromlng=121.54963921362912&tolng=121.56944464499509&fpoke=1&fgym=1&farm=0&nests=0&raids=1' --compressed" 

o = os.popen( c ).read()
a = json.loads(o) 

print a.keys()

l = []
for p in a.keys():
    print p, a[p]['rgqaca']
    c = "curl -s 'https://www.pokemongomap.info/includes/locdata.php' -H 'Cookie: PHPSESSID=3mcm776vrtlip9kv9556vl1fg7; mapfilters=1[##split##]1[##split##]1[##split##]0[##split##]0[##split##]1[##split##]0[##split##]0; announcement2=1; __atssc=reddit%3B1; announcementnews=1; __atuvc=1%7C27%2C6%7C28%2C8%7C29%2C1%7C30; __atuvs=5973efe889f467dd000; _ga=GA1.2.1811255488.1499521885; _gid=GA1.2.1712956306.1500725650; _gat=1; latlngzoom=17[##split##]24.81380027197877[##split##]121.02725218588863' -H 'Origin: https://www.pokemongomap.info' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://www.pokemongomap.info/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'mid="+p+"' --compressed"
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
