import os, time
from brain import core

path = os.getcwd()

if __name__ == '__main__':
    article = input("Url to article: ")
    if article.find("cnn") != -1:
        article_text = core.Jinx.get_article_cnn(article, core.Jinx)
    else:
        article_text = core.Jinx.get_article_fox(article, core.Jinx)
    prompt = f"{article_text} \nCan you summarize this article for me and give me the overall sentiment as a with a percentage:"
    answer = core.Jinx.GPT(prompt)
    print(answer)
    
    #################
    # Links to test #
    #################
    # https://www.cnn.com/2023/02/02/us/tyre-nichols-investigation-thursday/index.html
    # https://www.foxnews.com/politics/ilhan-omar-gets-boot-house-votes-off-foreign-affairs-committee-democrats-cite-racism