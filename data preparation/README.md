#Data Preparation

#### Sentiment Analysis
- Author: Abrar

We used [textblob](https://textblob.readthedocs.io/en/dev/) to analysis sentiment.
The function TextBlob() can take string as an input. And the function .sentiment returns the sentimental score of the particular string.

Example:
- TextBlob("good").sentiment
- Output: Sentiment(polarity=0.7, subjectivity=0.6000000000000001)

Here Polarity means how much positive or negative meaning the text has. Suppose good is positive word and bad is a negative word. Polarity scaled between -1 to +1. -1 means the extremely negative meaningful text. +1 means the most positive text.

Subjectivity means how much subjective the text is. e:g: opinion, emotion expressed in the text. Subjectivity scaled between 0 and +1.

We can get polarity and subjectivity as numeric by using following functions
- TextBlob(text).sentiment.polarity
- TextBlob(text).sentiment.subjectivity

