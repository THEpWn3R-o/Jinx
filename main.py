import os, time
from brain import core

path = os.getcwd()

if __name__ == '__main__':
    article = input("Url to article: ")
    article_text = core.Jinx.get_article_cnn(article, core.Jinx)
    prompt = f"{article_text}, Can you summarize this article for me: "
    answer = core.Jinx.GPT(prompt)
    print(answer)