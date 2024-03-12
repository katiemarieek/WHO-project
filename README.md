## WHO Project
Project conducted through the _Digital Futures Academy_.

### Objective

The aim of this project was to create a Machine Learning Model capable of predicting Life Expectancy from a set of data pertaining to a country's population in a given year. The deliverables were two models: one using all necessary data to achieve the best RMSE, and one using limited data to promote ethical data handling.

### Approach 

* We employed EDA to gain insights on the relationship between the feature columns and target, before training a Linear Regression model to predict life expectancy.
* We employed robust scaling to our feature engineered columns in order to reduce the Condition Number of our model, and used a Variance Inflation Function to reduce this further.
* We increased out R-squared value by using advanced OHE on the columns of Region and Country, in order to produce an encoding that retained positional information.
* Finally, we debated the ethical implication of each feature, in order to settle on our final selection.

### Results

We were able to produce a user interface to navigate our two models, taking the preferences of the user into consideration. Click below to try it for yourself!

https://who-predictor.streamlit.app/

Our results for our Accurate and Minimalist model are shown below.

#### Accurate Model

* R-squared value: 0.985
* RMSE on Train: 1.138
* RMSE on Test: 1.198

#### Minimalist Model

* R-squared value: 0.976
* RMSE on Train: 1.451
* RMSE on Test: 1.481
  
_Here's a quick guide on how to navigate this rep:_  

There are three folders:
* Code: Contains two files of python code, one pertaining to the EDA and Model Training process, and the other containing the functions built to hold the models.
* Data: Contains two files, one containing the WHO data, and one containing metadata.
* Streamlit: Contains three files, one containing the streamlit code for the User Interface, the second containing a pickled dictionary to be used with the User Interface, and the third all required modules as a requirements.txt file.
