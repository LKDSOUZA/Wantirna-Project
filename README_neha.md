# Credit Score Analysis

We tried to build a machine learning model that can classify the credit score ,upon given a person's credit-related information.

* source of data:

  https://www.kaggle.com/datasets/parisrohan/credit-score-classification?select=train.csv
  
* Data cleaning and creating machine learning model


  This dataset contains 28 columns, which are too many to handle and not all of them required to predict credit score.
   For this analysis our Target is 'Credit Score' which is string data type, converted this to int for training model.
 
    "poor" = 1, "standard" = 2, "good" = 3.
    
  For our Analysis we dropped certain columns which do not impact prediction and trained the model to get most important features for prediction.
  
 <img width="671" alt="Screenshot 2023-05-15 at 8 27 53 PM" src="https://github.com/LKDSOUZA/Wantirna-Project/assets/112359621/a9fe01c7-3163-4537-850f-1a2bd8d2086b">

Lastly,choosing the smaller dataset to train, dropping more columns had a big impact on achieving accuracy for our model.
