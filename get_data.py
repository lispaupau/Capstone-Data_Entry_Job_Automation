from bs4 import BeautifulSoup as bs
import requests


class GetData:
    def __init__(self):
        self.response = requests.get(url='https://appbrewery.github.io/Zillow-Clone/').text
        self.soup = bs(self.response, 'html.parser')
        self.hrefs = self.soup.find_all(class_='property-card-link')
        self.hrefs_list = [link['href'] for link in self.hrefs]

        self.prices = self.soup.find_all(class_='PropertyCardWrapper')
        replace_items = str.maketrans('', '', '$+bd/mo,\n')
        self.prices_list = [price.get_text().translate(replace_items).replace(' 1', '') for price in self.prices]

        self.addr = self.soup.find_all(class_='StyledPropertyCardDataArea-anchor')
        self.addr_list = [addr.get_text().strip() for addr in self.addr]

