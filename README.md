# Project-4  
## Wantirna Property Advisors

## Navigation prompts
Refer to file 'requirements.txt' for set-up and launch instructions

## Team members
- Javier Gausachs
- Neha Erande
- Lachlan D'Souza
- Hassan Jamil Malik

## Project description
2 Machine learning models were designed, 1 Model designed to predict the credit score of a user based on 9 features and the other model
designed to predict housing prices in Melbourne based on 19 features. Both models were saved using the Joblib. Flask was used to create the
application, using a form method to submit the related features to predict the credit score and housing prices. 

### Difficulties 
- Flask, submitting form. 


## Credit Score Analysis

We built a machine learning model that can classify the credit score, once the credit-related fields are filled by the user.

## Credit Score Dataset https://www.kaggle.com/datasets/parisrohan/credit-score-classification?select=train.csv

### Data cleaning and creating machine learning model


  This dataset contains 28 columns, which are too many to handle and not all of them required to predict credit score.
   For this analysis our Target is 'Credit Score' which is string data type, converted this to int for training model.
 
    "poor" = 1, "standard" = 2, "good" = 3.
    
  For our Analysis we dropped certain columns which do not impact prediction and trained the model to get most important features for prediction.
  
 <img width="671" alt="Screenshot 2023-05-15 at 8 27 53 PM" src="https://github.com/LKDSOUZA/Wantirna-Project/assets/112359621/a9fe01c7-3163-4537-850f-1a2bd8d2086b">

Lastly,choosing the smaller dataset to train, dropping more columns had a big impact on achieving accuracy for our model.


#### From previously searched and interest in real estate, it was an honour to actual dig deep the features in predicting the house prices in Melbourne. 

## Data search and importation

#### Data was imported from Kaggle dataset, https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market
![dataset_reference](https://github.com/LKDSOUZA/Wantirna-Project/assets/118155597/83f4739b-bc4f-4e2a-9819-bd39b09ff0d2)

## Data Filtering and Model Selection

#### Data was imported in Jupyter notebook. The information of number of data features has been shown in the image below
#### The number of unique values of each feature has been presented in the following image
![df_info](https://github.com/LKDSOUZA/Wantirna-Project/assets/118155597/c57cecf6-4a4f-4bc7-99df-6ede48ad90eb) ![df_unique_ent](https://github.com/LKDSOUZA/Wantirna-Project/assets/118155597/c0107dc2-01ed-4306-8b8e-ee37f6cbc849)

### 1st Model selection

#### Simple linear model was selected including all the features results in, 
![simple_linear_model_with_allinputs](https://github.com/LKDSOUZA/Wantirna-Project/assets/118155597/3633bfe2-db62-47f9-9096-b84d5a62712f)

### 2nd Model selection

#### Linear model was selected and data was filtered with respect to the similarity matrix results, 
![similarity _matrix_result](https://github.com/LKDSOUZA/Wantirna-Project/assets/118155597/6526e70d-3ed1-44f8-9dfb-f7b474a2af11)

#### After training the model result based on Linear Model was,
![result_of_simple_linear_model](https://github.com/LKDSOUZA/Wantirna-Project/assets/118155597/cceda6ff-532c-42dc-8c78-14fd9b2b729b)

### 3rd Model selection
#### Random forest Regressor was selected for further analysis of the model and the model R2 result was achieved. gridsearchCv was used to adjust the paramters to reach maximum performance of the model. But it turns out the default parmaters show the best performance of the model
![random_forest_result](https://github.com/LKDSOUZA/Wantirna-Project/assets/118155597/8edefc83-9abe-4f21-bdcd-aedd9a3c1d35)

## Saving the model using Joblib method


