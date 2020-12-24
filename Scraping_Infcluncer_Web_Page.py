from bs4 import BeautifulSoup as sp 
import requests
import pandas as pd 

my_url=requests.get('https://starngage.com/app/global/influencer/ranking/morocco?page=10') #change the url and run
web_page= sp(my_url.content)
table=web_page.select('table')[0]
coulums = table.find('thead').find_all('th')
coulume_names=[c.string for c in coulums]
rows=table.find('tbody').find_all('tr')
l = []
for tr in rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)
df = pd.DataFrame(l, columns=coulume_names)
df.to_csv('infl_file10.csv') 
#you can do it in a for boucle that will be easy and buy some time 
