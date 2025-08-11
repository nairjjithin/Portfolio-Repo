
## Business Problem

### Description

Text documents are one of the richest sources of data for businesses: whether in the shape of customer support tickets, emails, technical documents, user reviews or news articles, they all contain valuable information that can be used to automate slow manual processes, better understand users, or find valuable insights. However, traditional algorithms struggle at processing these unstructured documents, and this is where machine learning comes to the rescue!

We’ll use a public dataset from the BBC comprised of 2225 articles, each labeled under one of 5 categories.

![Automatic_Document_classification_machine_learning](https://user-images.githubusercontent.com/49233119/82561717-77c23180-9b91-11ea-86b9-c38c664e8a99.png)


###### Problem Statement

- We are tasked with predicting the category of a news article using machine learning models.
- This could be useful to instantly predict category of an article ,for which it is not mentioned.
  Helpful in reducing manual task.

### Sources or Useful Links

- Source1: http://mlg.ucd.ie/datasets/bbc.html - Train and Validation data set.
- Source2: https://inshorts.com/ - Evaluation data set.(Collected through WebScrapping)

### Real World/Business objectives and Constraints

- Cost of misclassification can be high.
- Interpretability is partially important

## Machine Learning Problem

### Data Overview

- Consists of 2225 documents from the BBC news website corresponding to stories in five topical areas from 2004-2005.
- Class Labels: 5 (business, entertainment, politics, sport, tech).
- Size of bbc file:4.80MB.
- Scrapped data from https://inshorts.com/ for evaluation dataset.
- inshorts dataset contains 25 articles of 5 (business, entertainment, politics, sport, tech).

### Mapping Real World problem to Machine Learning problem

- Multiclass classification problem.For a given article we need to predict its caetgory among five classes.
- Train the model on BBC data.The model should be able to categorize article from any news source.

### Metrics

- Multiclass Confusion matrix- Macro avg F1score.
- Macro avg F1score=2*Pr_macro⋅Re_macro/(Pr_macro+Re_macro)
- If F1macro has a large value, this indicates that a classifier performs well for each individual class. 
  The macro-average is therefore more suitable for data with an imbalanced class distribution.

### Data Pre processing

- In this session we performed
    - Null value treatment.
    - Html&URL removal
    - Decontraction of words
    - lower case conversion
    - special characters removal
    - stop words removal.

### Feature Extraction steps

- Extracted first line of each articles and added a new featue-title.
- Gave more weightage to words in title.

### Vectorization

- Performed Tfidf-vectorization with min_df=5 and ngram=(1,2)

### Select-K best

- Used Selct K best method to get best 6000 features ,based on chi2 value .
- Helped to reduce dimentions and reduce impact of overfitting.

### Model Building ,validation and Evaluation

- Performed model validation using unseen bbc articles with Logistic regression,SVM and Random Forest methods.
- Performed model evaluation on data scrapped from inshorts.com with Logistic regression,SVM and Random Forest methods.
- LogisticRegression is selected for Document classiffier application development.

## Summary & Conclusion

- We created train and validation data with articles from bbc.
- Extracted title from articles and added as a new feature.
- Treated the text features for htmls,urls,contracted words,stop words etc.
- Tested the model performance on train and validation data.
- Its been identified that the model is performing well on both train and validation data with accuraccy & F1_score of 100% on train 
  and 97%on test.
- Upon further analysis,its been understood that the high performance is due to facts that,
    - There are very few data points available.Which makes our model to overfit on data.This cause high accuraccy on train data.
    - both the train and validation set article belongs to bbc.Hence,the language structure of the articles may be the same.Which cause train and test data to be in similar to nature.And hence,high accuraccy on test data too.
- For forther evaluation,we webscrapped inshorts.com ,collected the articles from 5differrent categories and created an evaluation dataset.
- On evaluation dataset,model is giving high F1_Score of 100% on train and 76% on evaluation data.Which suggestec the model is overfitting.
- The model as not able to perform well with articles related to business and tech.
- To tackle overfittingwe gave more weightage to tile.Because,title itself contains lot of information.
- Selected best 6000 features using chi2 metric.
- On selected 6000 features,the model performance improved,eventhough that is not a substantial improvement.
- The model performace improved from 76% to 78% f1_score.
- The models ability to identify tech articles improved.
- The model performnce can be improved by increasing training records/samples.
- Training the model with articles from differrent sources can increase its ability to generalize on unseen data.
- Selecting best 6000 features can reduce the impact of overfitting.
- We perfomed model validation and evaluation with logistic regression,SVM and Random forest and OneVsRest approach.
 All three algorithms provided similar results.
- LogisticRegression with best 6000 features are selected for creating Document classifiaction application.
- Tkinter is selected to develop the front end.
