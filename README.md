# ensemble_learning
Ensemble learning project - Airbnb price prediction NYC 2019
Airbnb Price Prediction Using Ensemble Algorithms - README

Objective:
The objective of this project is to predict the optimal price for Airbnb listings using ensemble learning models. We aim to build a pricing model by taking into account the attributes of the listing.

Methodology
We followed a supervised regression approach to learn from the labeled data to predict the target variable. Our methodology consists of the following steps:

Data pre-processing: This step includes processes such as eliminating features with more than a certain percentage of missing values, replacing missing values, transforming the target variable, and normalizing data.
Data splitting: We split the dataset into a training set and a test set.
Modeling: We used ensemble learning algorithms to build the pricing model.
Model evaluation: We evaluated our models using various performance metrics.
Data Processing
We began by examining the dataset, which initially contained 48,895 observations and 16 variables. The target variable is 'price', which reveals the price per night of an Airbnb listing. The price in our dataset varies between $0 and $10,000. We also have good data on location of space (latitude, longitude, area name, and neighborhood). We dropped the variables 'id', 'name', and 'host_name' as they played a minimal role in our analysis.

Missing Values
As it is difficult to impute data that have a large number of missing values accurately, we replaced columns that contained more than 20% of missing values. We replaced missing values in the variable 'reviews_per_month' by taking the mean of all the values of this variable. We dropped the variable 'last_review' as it had 20% of missing values. We also verified that our target had no missing values.

Transforming Data
We used Log+1 transformation to make the feature 'price' less skewed as it had a positive skewness. This helped to make easier interpretation and better statistical analysis. After the transformation, the price had a normal distribution.

Removing Outliers
We removed outliers using the interquartile range method for the following variables: 'number_of_reviews', 'price', 'availability_365', and 'reviews_per_months.'

Exploratory Analysis
We conducted an exploratory analysis to gain insight from our data. For a question of space, the exploratory analysis will only be available by accessing the notebook Ensemble_Project.

Conclusion
Using ensemble learning algorithms, we built a pricing model for Airbnb listings that takes into account the attributes of the listing. Our model is based on a supervised regression approach, and we evaluated our models using various performance metrics. This project is helpful for Airbnb hosts who want to determine the optimal price for their listings.
