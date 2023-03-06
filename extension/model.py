# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import wordopt


# Importing the dataset
df_eng = pd.read_csv('English.csv')
df_fil = pd.read_csv('Filipino.csv')

# Prepare dataset
df_merge = pd.concat([df_eng, df_fil], axis=0)
df = df_merge.drop(["Page"], axis = 1)
df = df.sample(frac = 1) # shuffle dataset
df.reset_index(inplace = True)
df.drop(["index"], axis = 1, inplace = True)

# Define X and y
x = df["Text"]
y = df["Label"]

df["Text"] = df["Text"].apply(wordopt)  #apply wordopt function
df.to_csv('cleaned.csv')

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Convert text to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(x)
xv_train = vectorizer.transform(x_train)
xv_test = vectorizer.transform(x_test)
pickle.dump(vectorizer.vocabulary_, open('vectorizer.pkl','wb'))

# Using Support Vector Machine
classifier = LogisticRegression(solver='saga', penalty='l1', 
                                max_iter=1000, C=100)
classifier.fit(xv_train, y_train)

#evaluating the model
#pred_classfier = classifier.predict(xv_test)
#score = cross_val_score(classifier, X, y, cv=10)
#print(score.mean()) # score of the model with cv=10

# Saving model using pickle
pickle.dump(classifier, open('model_fakenews.pkl','wb'))
