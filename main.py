from scraper import get_games
from scraper import get_links
from scraper import scrape_songs
import requests
import pandas as pd
from time import sleep

# Get rid of pandas 'append' in line 26


def main():
    requested_html = requests.get(url='https://www.nhl.com/rangers/info/sounds-of-the-game')

    games = get_games(html=requested_html)
    links = get_links(html=requested_html)

    games_and_links_dict = {'Game': games,
                            'Link': links}

    games_and_links_df = pd.DataFrame(games_and_links_dict)

    scraped_songs_df = pd.DataFrame(columns=['Title', 'Artist', 'Period', 'Game'], index=None)

    for link in links:
        game = games_and_links_df.loc[games_and_links_df['Link'] == link, 'Game'].iloc[0]
        scraped_data = scrape_songs(url=link)
        scraped_data['Game'] = game
        scraped_songs_df = pd.concat([scraped_songs_df, scraped_data])

        sleep(4)

    scraped_songs_df.to_csv('full_data.csv')


if __name__ == '__main__':
    main()
