import pandas as pd
from fetcher import MongoLoader
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#
nltk.download('vader_lexicon')# Compute sentiment labels
# tweet = 'Skillcate is a great Youtube Channel to learn Data Science'

# score=SentimentIntensityAnalyzer().polarity_scores(tweet)
# print(score)



class Processing:
    def __init__(self):
       self.df =MongoLoader().get_all_data()

    def rare_word_in_text(self):
        if "Text" not in self.df.columns:
            raise ValueError("DataFrame must contain 'Text' column")
        rare_words = []
        for tweet in self.df["Text"]:
            all_words = pd.Series(tweet.lower().split())
            rarest_word = all_words.value_counts().idxmin()
            rare_words.append(rarest_word)
        self.df["rarest_word"] = rare_words


    def find_text_emotion(self):
        if "Text" not in self.df.columns:
            raise ValueError("DataFrame must contain 'Text' column")
        emotion = []
        for tweet in self.df["Text"]:
            score = SentimentIntensityAnalyzer().polarity_scores(tweet)
            compound = score["compound"]
            if compound > 0.5:
                emotion.append("Positive")
            elif compound == 0.49:
                emotion.append("Neutral")
            else:
                emotion.append("Negative")

        self.df["Emotion text"] = emotion
        self.df["_id"] = self.df["_id"].astype(str)
        return self.df

# a=Processing()
# a.find_text_emotion()
# print(a.df)
