#!/usr/bin/env python
import  sys
import  json
import  requests
import  time
import  os
from math import asin, atan, cos, exp, log, pi, sin, sqrt, tan
import  datetime

t = 'beipu'
c = "curl 'https://www.wecatch.net/md?pokemon=true&gyms=true&rares=false&f=A4%2BVtLgB4Qd3iara6nbjLTosaZyupIimrlnDrjY7EpfprCk8Q8EiVJP%2F8mncmQNqXBPs1zLogyfbUV6Bf646sFvDjzNQMIisy9PyS0LbfwBNIJnqKEfHe9%2Brz9pl4eSyT7McGD0txnGwkQzPpOejDXPVqc0ivQXCJ6Y4MugHA4UMdqq6GrC5WWG5SG47iK2xPVDNoYSz1S7g%2FtN4YVMzF0NzUn3PFDn8waUFe4xv%2B0UBT3u2wqn1CHNSl%2BAAO%2BMzj%2BlnrcRa4PE3m1NR1CNzw9%2FkQGSvzL4Jltiztxz63NuNsNJXsloLWPRD0vWfB1ZyOPVyYVTmXVcLCMQWysTTJw%3D%3D&w=24.8044219&x=120.9827328&y=24.84220&z=121.09260&filter_pk=%5B0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47%2C48%2C49%2C50%2C51%2C52%2C53%2C54%2C55%2C56%2C57%2C58%2C59%2C60%2C61%2C62%2C63%2C64%2C65%2C66%2C67%2C68%2C69%2C70%2C71%2C72%2C73%2C74%2C75%2C76%2C77%2C78%2C79%2C80%2C81%2C82%2C83%2C84%2C85%2C86%2C87%2C88%2C89%2C90%2C91%2C92%2C93%2C94%2C95%2C96%2C97%2C98%2C99%2C100%2C101%2C102%2C103%2C104%2C105%2C106%2C107%2C108%2C109%2C110%2C111%2C112%2C113%2C114%2C115%2C116%2C117%2C118%2C119%2C120%2C121%2C122%2C123%2C124%2C125%2C126%2C127%2C128%2C129%2C130%2C131%2C132%2C133%2C134%2C135%2C136%2C137%2C138%2C139%2C140%2C141%2C142%2C143%2C144%2C145%2C146%2C147%2C148%2C149%2C150%2C151%2C152%2C153%2C154%2C155%2C156%2C157%2C158%2C159%2C160%2C161%2C162%2C163%2C164%2C165%2C166%2C167%2C168%2C169%2C170%2C171%2C172%2C173%2C174%2C175%2C176%2C177%2C178%2C179%2C180%2C181%2C182%2C183%2C184%2C185%2C186%2C187%2C188%2C189%2C190%2C191%2C192%2C193%2C194%2C195%2C196%2C197%2C198%2C199%2C200%2C201%2C202%2C203%2C204%2C205%2C206%2C207%2C208%2C209%2C210%2C211%2C212%2C213%2C214%2C215%2C216%2C217%2C218%2C219%2C220%2C221%2C222%2C223%2C224%2C225%2C226%2C227%2C228%2C229%2C230%2C231%2C232%2C233%2C234%2C235%2C236%2C237%2C238%2C239%2C240%2C241%2C242%2C243%2C244%2C245%2C246%2C247%2C248%2C249%2C250%2C251%5D&filter_gym=%5B%5D' -H 'cookie: __cfduid=d7060a186b5228e2a162001967daf945d1519920053; _ga=GA1.2.107019864.1519920056; _gid=GA1.2.1349911777.1519920056' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'referer: https://www.wecatch.net/' -H 'authority: www.wecatch.net' -H 'x-requested-with: XMLHttpRequest' --compressed" 

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
    if p['team'] == 1 and len(p['details']) < 6 and p['raid_pokemon_id'] == 0:
        tag = '** '
    else:
        tag = '   '
    print tag, p['name'], "%s,%s" % ( p['location'][1], p['location'][0] ), p['team'], len(p['details']), datetime.datetime.fromtimestamp(p['last_modified'][0])
    if tag != '   ':
        mob = []
        for q in p['details']:
            mob.append( q['pokemon_cp'] )
            #print '  ', q['pokemon_id'], q['pokemon_cp'], q['iv']
        print ' ' * 10, mob
