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
    t = sys.argv[1:]
else:
    t = None
#l = raw_input( 'PKGET> ' )
#c = "%s" % l 
c = "curl 'https://pkget.com/fp.ashx?a=22.780217481816518&b=121.21602058410645&c=22.739060752221494&d=121.10933303833008&e=1_1&f=Wa9nv4jHQeuZDDVoPAE7L1F1T4Uohruoa0fJ5oRE4T9c9EmZwwoRUV0CYRpxHbw9&g=%2FJCf6dNcRKzllO8MNDHDzljXcaDBs0oW8PN%2FVjC8BpE%3D&h=&j=765' -H 'Cookie: __gads=ID=af258e6421716de8:T=1499504590:S=ALNI_MaKvNSE7KrDe58kpl789QZBygvy-w; pkgetcomL=1; ASP.NET_SessionId=twpov40xjyjskwmkh4sxyzsg; pkgetcomGen=1; ga=ga=1.1.222588955.1419666884; pkll=22.8733161%2C121.106414; _ga=GA1.2.1157477300.1498827654; _gid=GA1.2.1251719925.1502064279; pkllg=24.8202072%2C121.00795; pkgetcom=lat0=22.782037589123988&lng0=121.2165355682373&lat1=22.740881408137906&lng1=121.10984802246094' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://pkget.com/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed" 

o = os.popen( c ).read()
j = json.loads(o) 

print datetime.datetime.now()
clist = []
plist = []
for p in sorted( j['fp'], key=lambda x: ( x['a'], x['b'] ) ):
    if t and p['a'] in t:
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
    oo = order[0]
    for o in order:
        p = clist[o]
        print '##', p['a'], datetime.datetime.fromtimestamp(int(p['b'])/1000), "%s,%s" % ( p['c'], p['d'] ), p['e'], p['f'], p['h']
        print order.index(o)+1, '/', len(order), '  distance:', get_min_route.distance( plist[oo], plist[o] ) 
        raw_input( )
        os.system( 'set_gps.py %s,%s' % ( p['c'], p['d'] ) )
        oo = o
