import openai
import os, time
from brain import core

def open_file(file):
    with open(file, 'r') as f:
        return f.read()

# OpenAI API Key, plus some varibles 
path = os.getcwd()
openai.api_key = open_file('brain/apikey.txt')

article = core.Grabber.get_article_cnn('https://www.cnn.com/2023/02/02/us/tyre-nichols-investigation-thursday/index.html', core.Grabber)

if __name__ == '__main__':
    print(article)