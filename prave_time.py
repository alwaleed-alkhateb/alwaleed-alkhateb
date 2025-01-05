import requests 
from pystyle import *
from bs4 import BeautifulSoup as bs 
# رسائل البداية
print(Box.Lines('Learn Python with Alwaleed'))
Write.Print('This program calculates the distance between two cities.\n', Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube('Example 12'))

ua={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
url=requests.get('https://timesprayer.com/prayer-times-in-buraydah.html',headers=ua)
soup=bs(url.content,'html.parser')
a1=soup.find(class_='info prayertable mobile').find_all('tr')[1].text
a2=soup.find(class_='info prayertable mobile').find_all('tr')[2].text
a3=soup.find(class_='info prayertable mobile').find_all('tr')[3].text
a4=soup.find(class_='info prayertable mobile').find_all('tr')[4].text
a5=soup.find(class_='info prayertable mobile').find_all('tr')[5].text
a6=soup.find(class_='info prayertable mobile').find_all('tr')[6].text



print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)