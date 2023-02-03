# Currently using model from https://github.com/vyashemang/flask-salary-predictor/
# More detailed tutorial thru https://towardsdatascience.com/deploy-a-machine-learning-model-using-flask-da580f84e60c

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from model import wordopt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)
model = pickle.load(open('model_fakenews.pkl', 'rb'))
tfidf = TfidfVectorizer(vocabulary=pickle.load(open("vectorizer.pkl", "rb")))

def output_lable(n):
    if n == 0:
        return "NOT Fake news"
    elif n == 1:
        return "Fake News"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    news = [x for x in request.form.values()]
    df = pd.read_csv("cleaned.csv")
    x = df["Text"]
    y = df["Label"]
    X = tfidf.fit_transform(x)
    inp = {"text": news}
    dataframe =  pd.DataFrame(inp) # similar to vectorization
    dataframe["text"] = dataframe["text"].apply(wordopt) # preprocessing
    x_test = dataframe["text"] 
    final_features = tfidf.transform(x_test)
    prediction = model.predict(final_features) # prediction part
    output = prediction[0] # get 1st value in the list
    
    return render_template('index.html', prediction_text='News is {}'.format(output_lable(output)))

    

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
