# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

def mars_news(browser):
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    browser.is_element_present_by_css('div.list_text', wait_time=1)
   
    html = browser.html
    newssoup = soup(html, "html.parser")

    try:
        sidebar = newssoup.select_one('div.list_text')

        news_title = sidebar.find('div', class_='content_title').get_text()
        news_p = sidebar.find_all('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return " ", " "

    return news_title, news_p


def featured(browser):

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    full_button = browser.find_by_tag('button')[1]
    full_button.click()

    html = browser.html
    featured_image = BeautifulSoup(html, 'html.parser')

    try:
        featured_image_url = featured_image.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return " "

    url_printed = f'https://spaceimages-mars.com/{featured_image_url}'

    return url_printed


def mars_facts():
    try:
        df = pd.read_html('https://galaxyfacts-mars.com/')[0]

    except BaseException:
        return " "
    df.columns=['Facts','Mars','Earth']
    df.set_index('Facts', inplace=True)

    return df.to_html(classes="table table-striped")

def hemispheres(browser):
    
    url = 'https://marshemispheres.com/'

    browser.visit(url)

    fourhemispheres = []


    for x in range(4):

        Enhanced = browser.find_by_tag('h3')[x]
        Enhanced.click()

        html = browser.html
        images = soup(html, 'html.parser')


        Image_url = images.find('img', class_='wide-image').get('src')
        urlprinted = f'https://marshemispheres.com/{Image_url}'

    
        title = images.find('h2', 'title').text
        title
    
        Dictionary = {
            'imgages': urlprinted,
            'title': title
            }
        
        fourhemispheres.append(Dictionary)

        browser.back()   
    return hemispheres



if __name__ == "__main__":

    print(scrape_all())