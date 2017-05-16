import requests
from bs4 import BeautifulSoup
import urllib.request
import os

i=0
tot=''
def trade_spider(search,max_pages):
    page = 1
    temp='http://finda.photo/search?q=' + search
    source_code = requests.get(temp, allow_redirects=False)
    plain_text = source_code.text.encode('ascii', 'replace')
    soup = BeautifulSoup(plain_text, 'html.parser')
    link=soup.find('strong')
    global tot
    tot=str(link)[8:-9]
    totnum=int(tot)
    while i<totnum:
        url = temp + '&page=' + str(page)
        source_code = requests.get(url, allow_redirects=False)
        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('div', {'class': "box"}):
            aid = link.get('data-image-id')
            down(search,'http://finda.photo/image/'+aid+'/thumbnail/original')
        page += 1

def down(word,url):
    global i
    i=i+1
    name="C:\\Users\\nhc75\\Desktop\\파제연구\\"+word
    if not os.path.exists(name):
        os.makedirs(name)
    name=name+'\\'+str(i)+ ".jpg"
    urllib.request.urlretrieve(url,name)
    print(str(i)+'/'+tot+' images searched')

trade_spider('person',15)
print('total '+str(i)+'images')
