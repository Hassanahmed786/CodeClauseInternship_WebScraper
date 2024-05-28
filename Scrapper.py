import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/city/delhi"

r = requests.get(url)
htmlContent = r.content
print(htmlContent)

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())	# to print html in tree structure

markup = "<p><!--this is comment--></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)

title = soup.title

#Get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)

 
print(soup.find('p'))

print(soup.find('p') ['class'])

print(soup.find_all("p",class_="lead"))

print(soup.find('p').get_text())
print(soup.get_text())

#Get all the anchor tag  from the page
anchors = soup.find_all('a')

all_links = set()

for link in anchors:
    if(link != '#'):
        link = "https://timesofindia.indiatimes.com/city/delhi" +link.get('href')
        all_links.add(link)
        print(link)

exit()

