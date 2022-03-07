import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# r = requests.get(url='https://www.nhl.com/rangers/fans/sounds-of-the-game-100418')

# with open('rangers_html.html', 'w') as file:
#     file.write(r.text)

# with open('rangers_html.html', 'r') as file:
#     html_code = file.read()


requested_html = requests.get(url='https://www.nhl.com/rangers/info/sounds-of-the-game')

# with open('rangers_games_html.html', 'w') as file:
#     file.write(r.text)

# with open('rangers_games_html.html', 'r') as file:
#     html_code = file.read()


def get_games(html):
    soup = BeautifulSoup(html, 'html.parser')

    html_games = soup.find_all('td')

    games_list = []

    for game in html_games:
        games_list.append(game.text)

    games_list = [game for game in games_list if game not in "Click for Playlist"]

    return games_list


def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')

    html_links = soup.find_all('a', string='Click for Playlist')

    links_list = []

    for link in html_links:
        links_list.append(link.get("href"))

    return links_list


games = get_games(requested_html)
links = get_links(requested_html)

games_dict = {"Game": games,
              "Link": links}

df = pd.DataFrame(data=games_dict)
print(df)

# df.to_csv("games.csv")

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

