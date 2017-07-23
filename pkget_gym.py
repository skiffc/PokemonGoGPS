#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
from math import asin, atan, cos, exp, log, pi, sin, sqrt, tan
import  datetime

t = 'beipu'
c = "curl 'https://pkget.com/getgym.ashx?a=24.869695292084224&b=121.16074562072754&c=24.833246145907253&d=121.05088233947754&e=0&f=&g=&h=&j=765' -H 'Cookie: ASP.NET_SessionId=4313y42kxovkxkclg4m4s1ue; __gads=ID=af258e6421716de8:T=1499504590:S=ALNI_MaKvNSE7KrDe58kpl789QZBygvy-w; pkgetcomL=1; pkgetcomGen=1; pkll=24.7895503%2C121.008911; pkllg=24.8201932,121.00792289999998; ga=ga=1.1.222588955.1419666884; _ga=GA1.2.1157477300.1498827654; _gid=GA1.2.801311312.1500209470; pkgetcom=lat0=24.86868296084082&lng0=121.16005897521973&lat1=24.83223351635245&lng1=121.05019569396973' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://pkget.com/igym.aspx' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed"

if len(sys.argv) > 1:
    if sys.argv[1] in ( 'cb' ):
        t = 'chubei'
        c = "curl 'https://pkget.com/getgym.ashx?a=24.826547058109924&b=121.0488224029541&c=24.800604149459257&d=120.93990325927734&e=0&f=&g=&h=&j=765' -H 'Cookie: ASP.NET_SessionId=4313y42kxovkxkclg4m4s1ue; __gads=ID=af258e6421716de8:T=1499504590:S=ALNI_MaKvNSE7KrDe58kpl789QZBygvy-w; pkgetcomL=1; pkgetcomGen=1; pkll=24.7895503%2C121.008911; pkllg=24.8201932,121.00792289999998; ga=ga=1.1.222588955.1419666884; _ga=GA1.2.1157477300.1498827654; _gid=GA1.2.801311312.1500209470; pkgetcom=lat0=24.82919557799801&lng0=121.04933738708496&lat1=24.803253223895933&lng1=120.9404182434082' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://pkget.com/igym.aspx' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed"
    else:
        t = 'hsinchu'
        c = "curl 'https://pkget.com/getgym.ashx?a=24.801850779773943&b=121.02436065673828&c=24.765381666521865&d=120.91449737548828&e=0&f=&g=&h=&j=765' -H 'Cookie: ASP.NET_SessionId=4313y42kxovkxkclg4m4s1ue; __gads=ID=af258e6421716de8:T=1499504590:S=ALNI_MaKvNSE7KrDe58kpl789QZBygvy-w; pkgetcomL=1; pkgetcomGen=1; pkll=24.7895503%2C121.008911; pkllg=24.8201932,121.00792289999998; ga=ga=1.1.222588955.1419666884; _ga=GA1.2.1157477300.1498827654; _gid=GA1.2.801311312.1500209470; pkgetcom=lat0=24.801071637296058&lng0=121.02693557739258&lat1=24.764602295034425&lng1=120.91707229614258' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://pkget.com/igym.aspx' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed"

print t

o = os.popen( c ).read()
j = json.loads(o) 

print j.keys()
for p in j['fp']:
    if p['b'] == 'Mystic' and int(p['e']) < 6:
        leading = '**'
    else:
        leading = '  '
    print leading, p['b'], "%s,%s" % ( p['c'], p['d'] ), p['e'], p['g']
