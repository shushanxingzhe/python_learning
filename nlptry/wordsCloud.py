from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba


with open("report19.txt", 'r', encoding='UTF-8') as f:
    mytext = f.read()
    mytext = " ".join(jieba.cut(mytext))
    wordcloud = WordCloud("simsun.ttf").generate(mytext)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()