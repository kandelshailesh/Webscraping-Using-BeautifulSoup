from urllib.request import urlopen
from bs4 import BeautifulSoup
html= urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsobj=BeautifulSoup(html.read(),"lxml")
try:  
     badcontent= bsobj.h1
except AttributeError as e:
     print("Tag was not found")
else:
     print(badcontent)
namelist= bsobj.findAll("span",{"class":"green"})
for name in namelist:
     print(name.get_text())

with open('C:/Users/Anonymous1/Desktop/node+react/fip/public/index.html') as htmlfile:
     soup=BeautifulSoup(htmlfile,'lxml')
print(soup.prettify())
     
     
local=urlopen("http://localhost:3000")
localdata=BeautifulSoup(local.read(),"lxml")
print(localdata.prettify())
