import requests,sys,colorama
from colorama import Fore, Style
from bs4 import BeatifulSoup
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
file = open(sys.argv[1],'r').read().split('\n')
for link in file:
	print(Fore.RED,"[IP]=>["+link+"]")
	if link == '':
		continue
	url = "https://viewdns.info/reversip/?host="+link"&t=1"
	text = requests.get(url,headers=header)
	soup = BeautifulSoup(text,'html.parser')
	nar = soup.find('table',attrs={'border':'1'})
	if narr == None:
		continue
	domaine = nar.findAll('td',attrs={'align':None})[2:]
	for line in domaine:
		if line == '':
			continue
		print(Fore.YELLOW,line.text)
print(Fore.RED,"ALL DONE !")
