# Predicting Food Ratings Based on Recipe Data 


## Research Question:

- Finding the rating of a food (supervised learning)


## Task for data cleaning and EDA:
•	Convert observations in CookTime column, PrepTime column and TotalTime column form hours to minutes (**done**)

•	NA’s in CookTime columns should not be removed, but rather convert NA’s to 0 minutes. (**done**)

•	Columns to be removed are : Date published, Description, Images, RecipeKeywords, RecipeIngredrientsQuantities, RecipeServed, Recipeyield, RecipeInstructions. (**we will not remove now**)

•	With Recipe category column, we can do reduce some categories and do some cluster analysis which is optional. (**will moved to EDA PLAN**)

•	RecipeIngredrientParts, its all text we can convert to nominal field and can use that in the prediction model, and predict if the number of ingredients has any effect on ratings, considering the other dependent variables. (**will moved to Reseach question**)

•	We will change the column names to make them easier to understand.

•	We will do the summary,min,max ,their find the distributions for the continuous variables. (**will moved to EDA**)

•	For EDA we will do a PCA to reduce dimensionality for the following  columns: Calories, FatContent, SaturatedFatContent, CholestrolContent, SodiumContent, CarbohydrateContent, FibreContent, SugarContent, ProteinContent. (**will moved to EDA**)

•	In the review dataset,review column we can do some sentiment analysis, and make some positive or negative scoring and adding the analysis to our main data set. (**done**)


##### Major data cleaning tasks are done - 28 Feb. 


## HPCI TASK
1. Number of Ingerdients for each recipies using HPCI. Assigned to **Eunice** (done)

2. the minimum rating, maximum rating and average rating and number of count, we will create 2 more columns. Assigned to **Ravinder** (done)

3. Converted Likert scale to numerical value and group by receipie Id. Assigned to **Abrar** (done)



## EDA PLAN

- Plot for viewing no of null instances  (nanier)  - Ravinder
- Correlation plot of numerical things - Abrar
- Scatter plot of rating with any factors etc - Ravinder
- Histograms of numeric variables - Eunice
- Boxplot for reviews  - Eunice
- Geom Sommoth plotting for highly correlated variables - Abrar


## Machine Learning Task


- Random Forest - Ravinder
- SVM - Abrar
- Decision Tree or KNN - Eunice

<img src="https://i.ibb.co/zQYp1JZ/asjk.jpg" alt="drawing" width="600"/>



