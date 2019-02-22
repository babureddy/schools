import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url="http://www.studyguideindia.com/Schools/alphabet-LETTER-page-PAGE.html"
letters='abcdefghijklmnopqrstuwxyz'
for letter in letters:
    try:
        url1 = url.replace('LETTER',letter)
    except Exception as e:
        print (e)
        continue
    for i in range(1,100):
        try:
            u=url1.replace('PAGE',str(i))
            html = urllib.request.urlopen(u, context=ctx).read()            
            print (u)
        except:
            break
        schools=[]
        bs=BeautifulSoup(html, "lxml")
        a = bs.find_all('a')
        s=""
        for x in a:
            if 'title' in x.attrs.keys() and 'href' in x.attrs.keys() and 'id' in x.attrs.keys():
                name=x.attrs['title']
                m=x.attrs['href']                
                location=m[m.rfind('-')+1:m.find('.html')]
                s += "\n"+name+'\t'+location
        f=open('schools.txt','a')
        f.write(s)
        f.close()
