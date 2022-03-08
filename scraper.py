import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_games(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    html_games = soup.find_all('td')

    games_list = []

    for game in html_games:
        games_list.append(game.text)

    games_list = [game for game in games_list if game not in "Click for Playlist"]

    return games_list


def get_links(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    html_links = soup.find_all('a', string='Click for Playlist')

    links_list = []

    for link in html_links:
        links_list.append(link.get("href"))

    return links_list


def scrape_songs(url):
    html = requests.get(url=url)

    soup = BeautifulSoup(html.text, 'html.parser')

    songs = soup.find('table', class_='table-token__table stats_table')

    songs_df = pd.read_html(str(songs))[0]
    songs_df.columns = ['Title', 'Artist']

    songs_df['NaN_Check'] = (songs_df['Artist'].isnull()) & (songs_df['Title'].notnull())

    periods = []
    period = ''

    for row in songs_df.itertuples():
        # Check if 'NaN_Check' is True - these rows are periods (1st, 2nd, intermissions, etc)
        if row[3]:
            # Identify period by 'Track' column
            period = row[1]
            periods.append(period)
        else:
            periods.append(period)

    songs_df['Period'] = periods
    songs_df = songs_df.drop(['NaN_Check'], axis=1)
    songs_df = songs_df[songs_df['Artist'].notnull()]

    return songs_df



