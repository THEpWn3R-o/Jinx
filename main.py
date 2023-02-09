import os, time
from brain import core

path = os.getcwd()

if __name__ == '__main__':
    article = input("Url to article: ")
    article_text = core.Jinx.get_article(article, core.Jinx)

    prompt = f"{article_text} \nCan you summarize this article for me and give me the overall sentiment as a with a percentage:"
    answer = core.Jinx.GPT(prompt)
    print(answer)
    
    #################
    # Links to test #
    #################
    # https://www.cnn.com/2023/02/02/us/tyre-nichols-investigation-thursday/index.html
    # https://www.foxnews.com/politics/ilhan-omar-gets-boot-house-votes-off-foreign-affairs-committee-democrats-cite-racism
    # https://medium.com/@x_TomCooper_x/ukraine-war-1-february-2023-operational-level-e87baf595f45