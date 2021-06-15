from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np

import pickle


def word_divide_char(inputs):
    characters=[]
    for i in inputs:
        characters.append(i)
    return characters
loaded_model=pickle.load(open('model.pickle', 'rb'))
loaded_vecorizer=pickle.load(open('vectorizer.pickle', 'rb'))
# load the model from disk

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/StrenghChecker',methods=['POST'])
def StrenghChecker():
  
    password=''
    password=request.form.get("pass")
    print(password)
    X_predict=np.array([password])
    X_predict=loaded_vecorizer.transform(X_predict)
    y_pred=loaded_model.predict(X_predict)
    if y_pred.item()==0:
        strength="LOW"
    elif y_pred.item()==1:
        strength="MEDIUM"
    else:
        strength="STRONG"
    
    return render_template('home.html', strength=strength)
    
    


if __name__ == '__main__':
	app.run(debug=True)
