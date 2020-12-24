#Load the necessary Libraries
import requests
from bs4 import BeautifulSoup as sp
#Load our first page
    #load the webpage content
my_url =requests.get('https://displate.com/browse-collections/landscapes/bestselling')
    #convert to bs object
soup = sp(my_url.content)
    #print out our html
print(soup)
 print(soup.prettify())
    #find and find all
first_header=soup.fin('h2')
divs=soup.find_all('div')
    #pass a list of element to look for
 list_div_iframe=soup.find(['div','iframe'])
    #you can in  attributes to find/finall dunctions
rdiv=soup.find_all('div',attrs={'class':'footer_payments'})
    #you can nest fin/findall
body= soup.find('body')
div=body.find('div')

    #we can search specific string
 paraghraph = soup.find_all("p",string="some")
import re
 paraghraph = soup.find_all("div",string=re.compile("some"))
#Changing the url
my_url= requests.get(' https://keithgalli.github.io/web-scraping/example.html')
soup = sp(my_url.content)
    #Select method (CSS method)
content = soup.select("p")
        #Selct p inside div
content =soup.select('div p')
        #Selcet the p after h2
par=soup.select("h2 ~ p")
        #Selcet the b after p with id class
bold=soup.select("p#paragraph-id b")
        #nested select
 par=soup.select("body > p")
for paraghraph in par: paraghraph.select("i")
        #Grab bu element with specific property
soup.select('[align=middle]')
    #Get different properties of the HTML
header = soup.find('h2')
print(header)
print(header.string)
        #if we have more than one string
print(div.get_text())
        #gettinh a specific property  from an element
link=soup.find('a')
link['href']
par = soup.select('p#paragraph-id')
print(par[0]['id'])
#Code Navigation
    #Path syntax
soup.body.div.h1.string
    #Know the terms : parent; sibling,child
soup.body.find('div').find_next_siblings()


#Practice
    #EX1 Grab all social links
 my_url=requests.get('https://keithgalli.github.io/web-scraping/webpage.html')
 soup=sp(my_url.content)
print(soup.prettify())
 social=soup.find('ul',attrs={'class':'socials'}) 
 print(social.get_text())
        #or
social=soup.select('ul.socials a')
actual_links = [link['href'] for link in social ]
    #EX2 Scrape an html table into a pandas datafra
import pandas as pd 
table = soup.select("table.hockey-stats")[0]
coulums = table.find('thead').find_all('th')
coulume_names=[c.string for c in coulums]
rows=table.find('tbody').find_all('tr')

l = []
for tr in rows:
    td = tr.find_all('td')
    row = [str(tr.string).strip() for tr in td]
    l.append(row)
df = pd.DataFrame(l, columns=coulume_names)
    #EX2 Grab all fun facts that contain the world 'is'
facts=soup.select('ul.fun-facts li')
facts_with_is=[fact.find(string=re.compile('is'))for fact in facts]

            #mine
fun_facts=soup.find('ul',attrs={'class':'fun-facts'})
fun_facts_text= fun_facts.get_text()
 re=fun_facts_text.splitlines()
for i in re :
    if 'is' in i:
        print(i)
    #EX4 Use beautiful soup to help dpwload an image from a webpage
img=soup.select('div.row div.column img')
actual_links = [link['src'] for link in img ]
img1=actual_links[0]
url = "https://keithgalli.github.io/web-scraping/"
full_url = url + img1
img_data = requests.get(full_url).content
with open('lake_como.jpg', 'wb') as handler:
    handler.write(img_data)



# Done locally, but here is the code
import requests # pip install requests
from bs4 import BeautifulSoup as bs # pip install beautifulsoup4

# Load the webpage content
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url+"webpage.html")

# Convert to a beautiful soup object
webpage = bs(r.content)

images = webpage.select("div.row div.column img")
image_url = images[0]['src']
full_url = url + image_url

img_data = requests.get(full_url).content
with open('lake_como.jpg', 'wb') as handler:
    handler.write(img_data)

    # EX5 Solve the mystery challenge
r = requests.get("http://www.mywebsite.com/search/")
soup = BeautifulSoup(r.content)

for a_tag in files.find_all('a', href=True):
    print 'href: ', a_tag['href']

# Configure this to the root of the above website, e.g. 'http://www.mywebsite.com'
base_url = "https://keithgalli.github.io/web-scraping/"

for a_tag in soup.find_all('a', class_='listing-name', href=True):
    print '-' * 60      # Add a line of dashes
    print 'href: ', a_tag['href']
    request_href = requests.get(base_url + a_tag['href'])
    print request_href.content
files = webpage.select("div.block a")
relative_files = [f['href'] for f in files]
#response

url = "https://keithgalli.github.io/web-scraping/"
for f in relative_files:
  full_url = url + f
  page = requests.get(full_url)
  bs_page = bs(page.content)
  secret_word_element = bs_page.find("p", attrs={"id": "secret-word"})
  secret_word = secret_word_element.string
  print(secret_word)