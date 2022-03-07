import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# r = requests.get(url='https://www.nhl.com/rangers/fans/sounds-of-the-game-100418')

# with open('rangers_html.html', 'w') as file:
#     file.write(r.text)

# with open('rangers_html.html', 'r') as file:
#     html_code = file.read()


r = requests.get(url='https://www.nhl.com/rangers/info/sounds-of-the-game').text

soup = BeautifulSoup(r, 'html.parser')

games = soup.find('table', class_='table-token__table stats_table')

links = soup.find_all('a', string='Click for Playlist')

links_list = []

for link in links:
    links_list.append(link.get("href"))

print(links_list)

# df = pd.read_html(str(games))[0]['DATE']

# print(df)

# def scrape_songs(url):
#
#     requested_html = requests.get(url=url)
#
#     soup = BeautifulSoup(requested_html, 'html.parser')
#
#     songs = soup.find('table', class_='table-token__table stats_table')
#
#     df = pd.read_html(str(songs))[0]
#     df.columns = ['Title', 'Artist']

