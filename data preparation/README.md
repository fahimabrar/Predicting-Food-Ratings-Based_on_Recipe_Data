# Data Preparation

#### Sentiment Analysis
###### Author: Abrar

We used [textblob](https://textblob.readthedocs.io/en/dev/) to analysis sentiment.
The function TextBlob() can take string as an input. And the **sentiment** function returns the sentiment score of the particular string.

**Example:**
- TextBlob("good").sentiment
- Output: Sentiment(polarity=0.7, subjectivity=0.6000000000000001)

Here **Polarity** means how much positive or negative meaning the text has. e:g: good is positive word and bad is a negative word. 
Polarity scaled between -1 to +1.

-1 means the extremely negative meaningful text. +1 means the most positive text.

**Subjectivity** means how much subjective the text is. e:g: how much opinion, emotion expressed in the text. Subjectivity scaled between 0 and +1.

We can get polarity and subjectivity as numeric by using following functions
- TextBlob(text).sentiment.polarity
- TextBlob(text).sentiment.subjectivity

###### Data 
In our review dataset we have customers review for particular foods. We give this texts as input to TextBlob sentiment function. It returns polarity and subjectivity score for each review. we converted the score into different classes. 

Our main objective was to classify the review into lickert (or lickertlike) scale. Here we used five point scale

| Tables        |Polarity (%)           |
|:-------------:|:-------------:|
| Very Good      | >= 80 |
| Good      | Between 41 and 79     |
| Average | Between -40 to 40     |
| Poor     | Between -41 and -79      |
| Very Poor | <=-80     |

As review is very subjective, so for subjectivity we selected >50% for applying above scale. If subjectivity less/equal 50 we directly classify the review as "average"

After applying the abovementioned condition we generated a new column named *Review_classified* 

###### Exception

Null values in review column terminate the function giving errror. We converted nan into string. That have no value, so in sentiment analysis all the nan values gets "average" class

###### N:B
- The data cleaning was computationaly heavy. It processed 1.4 million rows and took good amount of time to execute the python file. 
- The 493MB cannot be uploaded on github









