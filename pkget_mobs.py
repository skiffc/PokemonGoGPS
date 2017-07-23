#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
from math import asin, atan, cos, exp, log, pi, sin, sqrt, tan
import  datetime
import  get_min_route 

if len(sys.argv) > 1:
    t = sys.argv[1]
else:
    t = None
#l = raw_input( 'PKGET> ' )
#c = "%s" % l 
c = "curl 'https://pkget.com/fp.ashx?a=24.83760814776757&b=121.05783462524414&c=24.797097934504578&d=120.95020294189453&e=1_1&f=STfxtbuRUqlxlUmC7xbUcQCxNbBm01bj11FoWhdWf0%2F5EAQLEkxVACoJLe3X43HH&g=Bp7ievLHmnZl5hmsnq26osCW7MApgIRiEMGZ0fvv9Jw%3D&h=&j=765' -H 'Cookie: ASP.NET_SessionId=4313y42kxovkxkclg4m4s1ue; __gads=ID=af258e6421716de8:T=1499504590:S=ALNI_MaKvNSE7KrDe58kpl789QZBygvy-w; pkgetcomL=1; pkgetcomGen=1; ga=ga=1.1.222588955.1419666884; pkll=25.0142564%2C121.522929; _ga=GA1.2.1157477300.1498827654; _gid=GA1.2.801311312.1500209470; _gat=1; pkllg=24.820224099999997,121.0079304; pkgetcom=lat0=24.84049010038582&lng0=121.06178283691406&lat1=24.799980829601843&lng1=120.95415115356445' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://pkget.com/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed" 

o = os.popen( c ).read()
j = json.loads(o) 

print datetime.datetime.now()
clist = []
plist = []
for p in sorted( j['fp'], key=lambda x: ( x['a'], x['b'] ) ):
    if t and t == p['a']:
        leading = '**'
        clist.append( p )
        plist.append( ( float(p['c']), float(p['d']) ) )
    else:
        leading = '  '
    print leading, p['a'], datetime.datetime.fromtimestamp(int(p['b'])/1000), "%s,%s" % ( p['c'], p['d'] ), p['e'], p['f'], p['h']
    #s = '%s %s %s %s,%s %s %s %s' % ( leading, p['a'], datetime.datetime.fromtimestamp(int(p['b'])/1000), p['c'], p['d'],  p['e'], p['f'], p['h'] )
    #print s

if t:
    order = get_min_route.get_route( plist )
    print order
    raw_input( 'Press to start:\n' )
    oo = 0
    for o in order:
        p = clist[o]
        print '##', p['a'], datetime.datetime.fromtimestamp(int(p['b'])/1000), "%s,%s" % ( p['c'], p['d'] ), p['e'], p['f'], p['h']
        print order.index(o), '/', len(order), '  distance:', get_min_route.distance( plist[oo], plist[o] ) 
        raw_input( )
        os.system( 'set_gps.py %s,%s' % ( p['c'], p['d'] ) )
