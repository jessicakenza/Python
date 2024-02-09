# le package requests est utilisé pour extraire les données a partir d'un site web
import requests
#parser les élements afin de parcourir le contenu d'un texte ou d'un fichier en l'analysant pour vérifier sa syntaxe ou en extraire des éléments.
#pour ca on utilise le package Beautiful Soup

import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extraire le titre de la page
title_tag = soup.find('title')
print("Titre de la page :", title_tag.text)

# Extraire les liens vers les actualités
news_links = soup.find_all('a', class_='gem-c-document-list__item-title')
for link in news_links:
    print("Texte du lien :", link.text)
    print("URL du lien :", link.get('href'))

# Extraire tous les paragraphes de la page
paragraphs = soup.find_all('p')

# Afficher le texte de chaque paragraphe
for paragraph in paragraphs:
    print(paragraph.text)
