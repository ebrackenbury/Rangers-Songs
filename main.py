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

    games_and_links_dict = {"Game": games,
                            "Links": links}

    games_and_links_df = pd.DataFrame(games_and_links_dict)

    scraped_songs = pd.DataFrame(columns=['Title', 'Artist', 'Period'])

    for link in links:
        scraped_data = scrape_songs(url=link)
        scraped_songs.append(scraped_data)
        print(link)

        sleep(5)

    scraped_songs.to_csv('full_data.csv')


if __name__ == '__main__':
    main()
