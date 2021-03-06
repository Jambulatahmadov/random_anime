from bs4 import BeautifulSoup
import requests
import random

DOMAIN = "https://yummyanime.club"

def pars():
	URL = DOMAIN + '/top'
	HEADERS = {
		'User-agent': 'Mozilla/5.0 (X11; Linux x86_64)'
	}

	response = requests.get(URL, headers=HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.findAll('div', class_ = 'anime-column') 
	ani = []

	for item in items:
		ani.append({
			'title': item.find('a', class_ = 'anime-title').get_text(strip=True),
			'link': item.find('a', class_ = 'anime-title').get('href')
		})
	
	random_anime = random.choice(ani)
	print(f'Название: {random_anime["title"]}\nСсылка: {DOMAIN + random_anime["link"]}')

pars()