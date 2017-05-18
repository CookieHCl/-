import requests
from bs4 import BeautifulSoup
import urllib.request
import os

i=0
successful=0
tot=''
totnum=0
name=''
def trade_spider(search,max_num):
    page = 1
    temp='https://pixabay.com/ko/photos/?orientation=&image_type=photo&cat=&colors=&q='+search
    source_code = requests.get(temp, allow_redirects=False)
    plain_text = source_code.text.encode('ascii', 'replace')
    soup = BeautifulSoup(plain_text, 'html.parser')
    link=soup.find('h1', {'class': "hide-xs"})
    global tot
    global totnum
    global name
    tot=str(link.contents[0])[:-8]
    totnum=int(tot.replace(',',''))
    print(tot+' images searched in the server')
    name="C:\\Users\\nhc75\\Desktop\\파제연구\\"+search+'-pixabay'
    if not os.path.exists(name):
        os.makedirs(name)
    if max_num<totnum and max_num!=0:
        totnum=max_num
    while i<totnum:
        url = temp + '&pagi=' + str(page)
        source_code = requests.get(url, allow_redirects=False)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('div', {'class': "item"}):
            src=link.a.img.get('src')
            if(src=='/static/img/blank.gif'):
                down(link.a.img.get('data-lazy'))
            else:
                down(src)
        page += 1

def down(url):
    global i
    global successful
    if i<totnum:
        i=i+1
        successful=successful+1
        name2=name+'\\'+str(i)+ ".jpg"
        try:
            urllib.request.urlretrieve(url,name2)
        except:
            f=open('errorlist.txt','a')
            f.write(str(i))
            f.close()
            successful=successful-1
            #print('error :(')
        else:
            print(str(successful)+'/'+str(i)+' images searched')

trade_spider('사람',0)
print('searched '+str(successful)+'/'+str(i)+' images')
