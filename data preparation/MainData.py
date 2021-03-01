#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Import required libraries
import pandas as pd
import re

# Load recipes data into a variable called recipes
recipes = pd.DataFrame(pd.read_csv("C:/Users/SLL26/Desktop/Data Science and Analytics/CS5706 MACHINE LEARNING/CS5811 Coursework/recipes.csv"))

# View top 3 values from the loaded dataset
recipes.head(3)


# In[18]:


# We can import a package from GitHub whic does exactly what we need, but i will build a new logic.
# URL : https://github.com/metomi/isodatetime
import metomi.isodatetime.parsers as parse
duration = parse.DurationParser().parse('PT1H30M')
duration.get_days_and_seconds()


# In[19]:



# Create a User Defined Function to convert ISO duration i.e PT3H40M into seconds.
# The function below removes PT from each observation and splits string based on keywords ("H", "M", "S") and converts in seconds

def time(var):
    time = 0
    text = str(var)
    # Remove PT from each observation
    text = text.replace("PT", "")
    # Checks the format and converts accordingly
    if text == 'nan':
        time = 0
    elif ('S' in text):
        time = 0
    elif ('H' in text) and ('M' in text):
        time = time + int(text.split('H')[0])*60 + int(text.split('H')[1].replace('M', ''))
    elif 'H' in text:
        time = time + int(text.replace('H', ''))*60
    elif 'M' in text:
        time = time + int(text.replace('M', ''))
    else:
        time = 'NA'
    return time

# Apply the function to all three columns related to duration
recipes["CookTime"] = recipes["CookTime"].apply(time)
recipes["PrepTime"] = recipes["PrepTime"].apply(time)
recipes["TotalTime"] = recipes["TotalTime"].apply(time)


# In[6]:


recipes.head()


# In[20]:


# Import required libraries
#!pip install textblob
import glob
import re
import pandas as pd
from textblob import TextBlob


# In[21]:


glob.glob("C:/Users/SLL26/Desktop/Data Science and Analytics/CS5706 MACHINE LEARNING/CS5811 Coursework/reviews.csv")


# In[22]:


reviews = pd.read_csv("C:/Users/SLL26/Desktop/Data Science and Analytics/CS5706 MACHINE LEARNING/CS5811 Coursework/reviews.csv")


# In[25]:


# User Defined Function to check the review text and convert it into a likert scale
# Likert Scale: very poor, poor, average, good, very good. Based on polarity and sensitivity.
def sentiment(x):
        text = str(x)
        polarity = TextBlob(text).sentiment.polarity*100
        sensitivity = TextBlob(text).sentiment.subjectivity*100
    
        if sensitivity > 50:
            if polarity>=0:
                if polarity >=40 and polarity <80:
                    return "good"
                if polarity >=80 and polarity <=100:
                    return "very good"
                if polarity <=39:
                    return "average"

            if polarity<0:
                polarity = polarity * -1
                if polarity <=39:
                    return "average"
                if polarity >=40 and polarity <80:
                    return "poor"
                if polarity >=80 and polarity <=100:
                    return "very poor"
        else:
            return "average"


# In[26]:


reviews.head()


# In[ ]:


reviews["Review"] = reviews["Review"].apply(sentiment)


# In[35]:


reviews.head()


# In[27]:


# view top three observations of the column named RecipeIngredientParts
recipes['RecipeIngredientParts'].head(3)


# In[29]:


# splitting each ingredient which is a string, with comma, then counting the number of strings in each list
i = []
for value in recipes['RecipeIngredientParts']:
    words = value.split(',')
    i.append(len(words))
    
print(words)


# In[31]:


# loading the count of strings in each list, creating a new column named IngredientsCount 
recipes['IngredientsCount'] = i


# In[33]:


# view top three observations
recipes.head(3)


# In[34]:


reviews = reviews[['RecipeId','Review','Review_classified']]


# In[ ]:


reviews.head()


# In[ ]:


#A function that convert likert scale to some score
review_list = ["very poor", "poor", "average", "good", "very good"]
def review_score(x):
        if x == review_list[0]:
            return 1
        elif x == review_list[1]:
            return 2
        elif x == review_list[3]:
            return 4
        elif x == review_list[4]:
            return 5
        else:
            return 3


# In[ ]:


# A function that convert score to likert scale string again
def review_class(x):
        if x >= 5:
            return review_list[4] 
        elif x >=4:
            return review_list[3]
        elif x >= 3:
            return review_list[2]
        elif x >= 2:
            return review_list[1]
        else:
            return review_list[0]


# In[ ]:


reviews["Review_Score"] = reviews["Review_classified"].apply(review_score)
# converting likert scale strings into score for furhter operation


# In[ ]:


group_data = reviews.groupby(['RecipeId'], as_index = False).sum()
#groupby data by unique recipies and the sum funciton for getting the total review score for a unique recipe
count_data = reviews.groupby(['RecipeId'], as_index = False).count()
#getting the count of review occurs for each recipie
#so that we can calcualte the average review score


# In[ ]:


group_data.head()


# In[ ]:


count_data = count_data[["RecipeId", "Review"]]
#selecting only the necessary columns


# In[ ]:


count_data.head()


# In[ ]:


reviews_score = group_data.merge(count_data,on='RecipeId')
#merge dataframe on RecipeId


# In[ ]:


reviews_score.head()


# In[ ]:


reviews_score["Average_Score"] = reviews_score["Review_Score"]/reviews_score["Review"]
#getting the average review score, which again will be converted to likert classes


# In[ ]:


reviews_score.head()


# In[ ]:


reviews_score["Review_Class"] = reviews_score["Average_Score"].apply(review_class)
#converting score to likert scale again


# In[ ]:


dataframe.head()


# In[ ]:


clean_data.to_csv("Reviews.csv", index = False)
#saving the data as a comma separated value file

