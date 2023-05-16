# Wantirna-Project

## Studies Importance

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


