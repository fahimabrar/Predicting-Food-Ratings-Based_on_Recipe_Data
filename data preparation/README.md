# Data Preparation

Original Data can be downloaded from following link: https://www.kaggle.com/irkaal/foodcom-recipes-and-reviews

### Sentiment Analysis
###### Author: Abrar

We used [textblob](https://textblob.readthedocs.io/en/dev/) to analysis sentiment.
The function TextBlob() can take string as an input. And the **sentiment** function returns the sentiment score of the particular string.

**Example:**

    TextBlob("good").sentiment
    
    Output: Sentiment(polarity=0.7, subjectivity=0.6000000000000001)

Here **Polarity** means how much positive or negative meaning the text has. e:g: good is positive word and bad is a negative word. 
Polarity scaled between -1 to +1.

-1 means the extremely negative meaningful text. +1 means the most positive text.

**Subjectivity** means how much subjective the text is. e:g: how much opinion, emotion expressed in the text. Subjectivity scaled between 0 and +1.

We can get polarity and subjectivity as numeric by using following functions
- TextBlob(text).sentiment.polarity
- TextBlob(text).sentiment.subjectivity

##### Data 
In our review dataset we have customers review for particular foods. We give this texts as input to TextBlob sentiment function. It returns polarity and subjectivity score for each review. we converted the score into different classes. 

Our main objective was to classify the review into likert (or likertlike) scale. Here we used five point scale

| Tables        |Polarity (%)           |
|:-------------:|:-------------:|
| Very Good      | >= 80 |
| Good      | Between 41 and 79     |
| Average | Between -40 to 40     |
| Poor     | Between -41 and -79      |
| Very Poor | <=-80     |

As review is very subjective, so for subjectivity we selected >50% for applying above scale. If subjectivity less/equal 50 we directly classify the review as "average"

After applying the abovementioned condition we generated a new column named *Review_classified* 

##### Exception

Null values in review column terminate the function giving errror. We converted nan into string. That have no value, so in sentiment analysis all the nan values gets "average" class



##### TextBlob has done amazing job for classifying reviews. Some examples shown below:

##### Very Good 

<img src="https://i.ibb.co/17xLsbK/verygood.jpg" alt="drawing" width="600"/>

##### Very Poor

<img src="https://i.ibb.co/9hC4jGp/verypoor.jpg" alt="drawing" width="600"/>



After getting all the sentiments for the reviews we then group them by recipie ID, so that we can merge them with our main dataset based on recipe ID. getting sentiment for each recipe is combination of some smaller tasks. e:g:

- assigning numeric value for each class e:g 5 for very good, 1 for very poor
- getting the average by applying the equation : sum(review score for individual recipe)/count(individul recipies)
- then again convert this score into likert scale class


##### N:B
- The data cleaning was computationaly heavy. It processed 1.4 million rows and took good amount of time to execute the python file. 
- The 493MB cannot be uploaded on github

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Time Format
###### Author: Ravinder

In our data we have duration for CookTime, PrepTime and TotalTime in ISO 8601 format i.e. PT2H45M.
We need to convert this into minutes for all three columns so that we can use it properly.

We will create a user defined fucnction which can identify the format and based on the values can convert the duration into minutes.

**Example:**
- CookTime = "PT3H30M"
- time(CookTime)
- Output: 210.0

Here the function converts the ISO 8601 duration into a string and then remove unwanted character, parse through the string based on pattern and then converts the duration into minutes.

##### Data 

In our recipes dataset we have CookTime, PrepTime and TotalTime in ISO 8601 format for all the recipes. We give this ISO 8601 format data into our user defined function "time" as input and the function returns duration as integer.

After applying the above mentioned function "time" we updated the columns CookTime, PrepTime and TotalTime with duration in minutes.

Note - We are converting NA values in CookTime to 0 mins and also we have some columns with data as PT0S, which means 0 seconds and we are converting that too into 0 mins.


##### Some examples shown below:

##### Before applying the function

![image](https://user-images.githubusercontent.com/79374661/109417486-c2dc6100-79bb-11eb-8c1c-2e782f83b47e.png)

##### After applying the function

![image](https://user-images.githubusercontent.com/79374661/109417504-d8ea2180-79bb-11eb-9157-d51e7ded6ca8.png)

##### N:B
- The data cleaning was computationaly heavy. It processed .2 million rows and took good amount of time to execute the python file. 
- The 690MB cannot be uploaded on github

---------------------------------------------------------------------------------------------------------------------------------------------------------------------


### Ingredients Count
##### Author : Eunice

In our data we have a column named RecipeIngredientParts which is all text. 

The text consists of list of ingredients for each recipe, examples are c("blueberries", "granulated sugar", "vanilla yogurt", "lemon juice"),  
c("saffron", "milk", "hot green chili peppers", "onions", "garlic", "clove", "peppercorns", "cardamom seed", "cumin seed", "poppy seed", "mace", "cilantro", "mint leaf", "fresh lemon juice", "plain yogurt", "boneless chicken", "salt", "ghee", "onion", "tomatoes", "basmati rice", "long-grain rice", "raisins", "cashews", "eggs")

we need to convert this nominal field to be a numerical field by counting the number of ingredients in each list, so we can use it for predictions.

we used loops to achieve this 

we first had each string seperated by comma

then counted number of strings in each list into a list of values.

we  formed a new column with the values 

we named the new column Ingredient_Count and added the new column to the recipe dataset.

**Example**

- Input 1 :  c("saffron", "milk", "hot green chili peppers", "onions", "garlic", "clove", "peppercorns", "cardamom seed", "cumin seed", "poppy seed", "mace", "cilantro", "mint leaf", "fresh lemon juice", "plain yogurt", "boneless chicken", "salt", "ghee", "onion", "tomatoes", "basmati rice", "long-grain rice", "raisins", "cashews", "eggs")
    
- Input 2 :  c("blueberries", "granulated sugar", "vanilla yogurt", "lemon juice") 

- Output 1 :  25

- Output 2 :  4

Here the function has counted the number of strings which are ingredients in each list

**Data**

we  formed a new column with the values 

we named the new column Ingredient_Count and added the new column to the recipe dataset


----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### MinMaxMeanPerRecipe
###### Author: Ravinder

This code will store min, max and mean Rating per RecipeId in three variables and these three variables can be added to your aggregated dataset.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### MergeDatasets
###### Author: Ravinder

Follow the steps in this file to merge all the datasets into 1 master dataset

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#### The main dataset can be found [here](https://drive.google.com/drive/folders/1e994fROr9T_5l22ywDcsYYDZITpx69lJ?usp=sharing)

