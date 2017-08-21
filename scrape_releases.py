from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def scrape_episodes():
    '''
    Scrapes and parses data off One Piece wiki
    Returns:
        string: formatted text for tweeting
    '''

    # 'current_episode.txt' contains the upcoming episode number
    f = open('../current_episode.txt')

    # ignore ssl certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_15%E2%80%93current)'
    html = urlopen(url, context = ctx).read()

    # find the tag by id, which is 'ep799' for episode 799
    soup = BeautifulSoup(html, 'html.parser')
    c_id = 'ep' + f.read().strip()
    current = soup.find(id = c_id)

    raw_title = current.next_sibling.next_sibling
    raw_date = raw_title.next_sibling.next_sibling

    # convert raw tag contents to strings
    chapter = str(current.contents[0])
    title = (str(raw_title.contents[0])).strip()
    date = str(raw_date.contents[0])

    formatted_tweet = 'Chapter ' + chapter + ' ' + title + ' releasing on ' + date
    return formatted_tweet
