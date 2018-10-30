import matplotlib.pyplot as plt
from wordcloud import WordCloud

def save_wordcloud(list_words, save_path, fig_width=900, fig_height=500):
    font_path = '../VL-Gothic-Regular.ttf'
    list_words_space = ' '.join(list_words)
    wordcloud = WordCloud(background_color='white', font_path=font_path, width=fig_width, height=fig_height).generate(list_words_space)
    plt.imshow(wordcloud)
    plt.savefig(save_path)
    plt.show()
