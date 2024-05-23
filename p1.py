import requests
from bs4 import BeautifulSoup

# URL of news website
url = 'https://www.webscraper.io/test-sites/e-commerce/allinone'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h2', class_='headline')

for headline in headlines:
    print(headline.text.strip())
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')


