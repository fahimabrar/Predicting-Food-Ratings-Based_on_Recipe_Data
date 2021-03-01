# Distributed Data Analysis - CS5811 


## Research Question:

- Finding the rating of a food (supervised learning)
- Finding the calories of a recipie (supervised learning)
- Clustering food in differt types (unsupervised learning)


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
1. Number of Ingerdients for each recipies using HPCI. Assigned to **Eunice**

2. the minimum rating, maximum rating and average rating and number of count, we will create 2 more columns. Assigned to **Ravinder**

3. Converted Likert scale to numerical value and group by receipie Id. Assigned to **Abrar** 

**Note:** HPCI task now can be done with normal python scripts. While developing the project it can be done with this time. 


## EDA PLAN

- what graph/chart we want to view will be added here. Along with clustering PCA etc. ......................


## Machine Learning Task
1..Machine learning task will be done after EDA

2.. We can consider multiple algo’s with Neuro Networks.

3.. We can consider multiple algo’s with Random forest to predict the rating.

