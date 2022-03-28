import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.scan-vf.net/my-hero-academia/chapitre-347/1") 
soup = BeautifulSoup(htmldata, 'html.parser') 
tag = soup.find('a')
print(type(tag))
print(tag.get('img-responsive scan-page'))
    