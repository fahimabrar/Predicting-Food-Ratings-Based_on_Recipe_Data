# Distributed Data Analysis - CS5811 
## Task for data cleaning and EDA:
•	Convert observations in CookTime column, PrepTime column and TotalTime column form hours to minutes

•	NA’s in CookTime columns should not be removed, but rather convert NA’s to 0 minutes.

•	Columns to be removed are : Date published, Description, Images, Recipe, Keywords, RecipeIngredrientsQuantities, RecipeServed, Recipeyield, RecipeInstructions.

•	With Recipe category column, we can do reduce some categories and do some cluster analysis which is optional.

•	RecipeIngredrientParts, its all text we can convert to nominal field and can use that in the prediction model, and predict if the number of ingredients has any effect on ratings, considering the other dependent variables.

•	We will change the column names to make them easier to understand.

•	We will do the summary,min,max ,their find the distributions for the continuous variables.

•	For EDA we will do a PCA to reduce dimensionality for the following  columns: Calories, FatContent, SaturatedFatContent, CholestrolContent, SodiumContent, CarbohydrateContent, FibreContent, SugarContent, ProteinContent.

•	In the review dataset,review column we can do some sentiment analysis, and make some positive or negative scoring and adding the analysis to our main data set.


## HPCI TASK
1.. Author ID  and Author name can be used in Mapreduce to find the minimum, maximum and average.

2., Reviews and the minimum rating, maximum rating and average rating and number of count, we will create 2 more columns.

3., HPCI for the count of ingredients in the RecipeIngredientsParts Column, Recipe Id will be the key value, RecipeIngredientsParts will be the input. The key value will be a list and based on the list you can count the number of ingredients and return a key and value, that will be key as the Recipe Id, and value as count


## Machine Learning Task
1..Machine learning task will be done after EDA

2.. We can consider multiple algo’s with Neuro Networks.

3.. We can consider multiple algo’s with Random forest to predict the rating.

