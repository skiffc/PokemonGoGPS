#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
import  datetime
import  get_min_route 
import  re

c = "curl 'https://data.magicalgo-cdn.com/_dbserver.php' -H 'origin: https://magicalgo.com' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: */*' -H 'referer: https://magicalgo.com/' -H 'authority: data.magicalgo-cdn.com' --data '&sysversion=2602&nformat=1&uukey=4e73a739eba299a0531bc2905f4d6dd1&action=viewData&gym=1&pokestop=1&pokesource_loc=&history_pokemonid=&loc1=35.70416180399428&loc2=139.78280858136716&extent_space_max=0.0274658203125&slowmode=&nearbygym=&localua=Mozilla%2F5.0+(Macintosh%3B+Intel+Mac+OS+X+10_12_6)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F66.0.3359.139+Safari%2F537.36' --compressed" 

l = []

o = os.popen(c).read()
w = open( 'web', 'w' )
w.write( o )
w.close()

for p in open( 'web' ):
    s = p.strip().split(';')
    if s[0] == 'a=g':
        print s[1], s[4], s[3], s[6] 
    elif s[0] == 'a=s':
        print s[1], s[2]
    else:
        continue

    g = re.sub( 'l=', '', s[1] ).split(',')
    l.append( ( float(g[0]), float(g[1]) ) )

o = get_min_route.get_route( l )
with open( 'route', 'w' ) as w:
    for p in o:
        w.write( '%f,%f\n' % l[p] )
