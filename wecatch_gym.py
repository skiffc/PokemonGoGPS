#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
from math import asin, atan, cos, exp, log, pi, sin, sqrt, tan
import  datetime

t = 'beipu'
c = "curl 'https://www.wecatch.net/md?pokemon=true&gyms=true&rares=false&f=gj4rOOGBSzrnW%2FewHYMh8yB8MkKZIcWcHIxuYl7HOYJi6DQP5un3I5pZwqS%2BAdUWjbGZWlz4f2vTDB46txsGFXQSop0HFuh%2FESO%2B9y68SCtKAYHYMMlHHmV%2FrfgOuqD%2B4MxGaiMMHxSJixEXsFLpjHxIyrHGlASMDTL9mRgLhBw%3D&w=24.81697&x=120.98745&y=24.837063&z=121.097317' -H 'accept-encoding: gzip, deflate, br' -H 'x-requested-with: XMLHttpRequest' -H 'accept-language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'referer: https://www.wecatch.net/' -H 'authority: www.wecatch.net' -H 'cookie: __cfduid=d9e1a9f29c6c68c8b94098401e6a37f431502976282; __BWfp=c1502977284586x3cad95538; _ga=GA1.2.376524551.1502976286' --compressed" 

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
for p in sorted( j['gyms'], key=lambda x: x['last_modified'][0] ):
    #print p
    if p['team'] == 1 and len(p['details']) < 6:
        tag = '** '
    else:
        tag = '   '
    print tag, p['name'], p['location'], p['team'], len(p['details']), datetime.datetime.fromtimestamp(p['last_modified'][0])
    if tag != '   ':
        for q in p['details']:
            print '  ', q['pokemon_id'], q['pokemon_cp'], q['iv']
