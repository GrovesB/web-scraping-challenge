# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


def mars_news(browser):
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    sidebar = soup.select_one('div.list_text')

    news_title = sidebar.find('div', class_='content_title')
    news_p = sidebar.find_all('div', class_='article_teaser_body')

    return news_title, news_p


def featured(browser):

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    full_button = browser.find_by_tag('button')[1]
    full_button.click()

    html = browser.html
    featured_image = BeautifulSoup(html, 'html.parser')

    featured_image_url = featured_image.find('img', class_='fancybox-image').get('src')
    featured_image_url

    url_printed = f'https://spaceimages-mars.com/{featured_image_url}'

    return url_printed
    

def mars_facts(browser):
    mars_facts = pd.read_html('https://galaxyfacts-mars.com/')[0]

    mars_facts.columns=['Facts','Mars','Earth']
    mars_facts.to_html()

    url = 'https://marshemispheres.com/'

    browser.visit(url)

browser.quit()


if __name__ == "__main__":

    print(scrape_all())