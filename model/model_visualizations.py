import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class mv():
    def __init__(self):
        '''
        This class hosts several functions for data visualizations
        '''
        pass

    def generate_hist(x, y):
        '''
        This creates a function call that plots a histogram
        '''
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(12, 5))
        sns.barplot(x, y, palette="ch:s=.25,rot=-.25")

    def generate_wordcloud(text): 
        '''
        This creates a function call that creates the wordcloud
        '''
        wordcloud = WordCloud(max_words=30, background_color='white',
                            relative_scaling = 1
                            ).generate(text)
        plt.subplots(figsize=(10, 10))
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()

    def generate_pie(sizes, colors, explode, cities):
        '''
        This creates a function call that plots a pie chart
        '''
        
        # initializing the chart with the predefined variables
        plt.pie(sizes, colors=colors, labels=cities, 
                autopct='%1.1f%%', startangle=90, 
                pctdistance=0.85, explode=explode, 
                shadow=True, radius=1)
        
        # drawing circle
        centre_circle = plt.Circle((0,0),0.60,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        
        # increasing aspect ration 
        plt.tight_layout()
        plt.show()