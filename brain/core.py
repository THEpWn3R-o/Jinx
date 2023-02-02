import time, os, requests
from datetime import date
from bs4 import BeautifulSoup
import logging

class Grabber:
    def __init__(self, brain):
        self.brain = brain
        self.logger = logging.getLogger('brain.core.Grabber')
        logging.basicConfig(filename=f'{date.today}.log', encoding='utf-8')
        self.logger.info('Grabber initialized')

    def get_article_cnn(url, self):
        self.url = url
        self.article = requests.get(self.url)
        self.logger = logging.getLogger('brain.core.Grabber')
        self.logger.info(f'Grabbed article from {self.url}')
        self.soup = BeautifulSoup(self.article.text, 'html.parser')
        self.article_body = self.soup.find('div', class_='article__content')
        self.article_text = []
        for p in self.article_body.find_all('p'):
            self.article_text.append(p.get_text())
        self.logger.info('Parsed article text')
        return self.article_text