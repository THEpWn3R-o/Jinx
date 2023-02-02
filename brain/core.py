import time, os, requests
from datetime import date
from bs4 import BeautifulSoup
import openai
import logging

class Jinx:
    def __init__(self):
        self.logger = logging.getLogger('brain.core.Grabber')
        self.today = date.today()
        self.today = self.today.strftime('%Y-%m-%d')
        logging.basicConfig(filename=f'brain/log/{self.today}.log')
        self.logger.info('Jinx initialized')
        openai.api_key = open('brain/apikey.txt', 'r').read()

    def get_article_cnn(url, self):
        self.url = url
        self.article = requests.get(self.url)
        self.logger = logging.getLogger('brain.core.Jinx')
        self.logger.info(f'Grabbed article from {self.url}')
        self.soup = BeautifulSoup(self.article.text, 'html.parser')
        self.article_body = self.soup.find('div', class_='article__content')
        self.article_text = []
        for p in self.article_body.find_all('p'):
            self.article_text.append(p.get_text())
        self.logger.info('Parsed article text')
        return self.article_text
    
    def get_article_fox(url, self):
        self.url = url
        self.article = requests.get(self.url)
        self.logger = logging.getLogger('brain.core.Jinx')
        self.logger.info(f'Grabbed article from {self.url}')
        self.soup = BeautifulSoup(self.article.text, 'html.parser')
        self.article_body = self.soup.find('div', class_='article-content')
        self.article_text = []
        for p in self.article_body.find_all('p'):
            self.article_text.append(p.get_text())
        self.logger.info('Parsed article text')
        return self.article_text

    def GPT(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=256, freq_pen=0.0, pres_pen=0.0, stop=['<END>']):
        prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
        response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
        text = response['choices'][0]['text'].strip()
        return text


Jinx.__init__(Jinx)