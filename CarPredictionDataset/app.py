# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:38:27 2021

@author: krishna reddy
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    Year = int(request.form['Year'])
    Present_Price=float(request.form['Present_Price'])
    Kms_Driven=int(request.form['Kms_Driven'])
    Kms_Driven2=np.log(Kms_Driven)
    Owner=int(request.form['Owner'])
    Fuel_Type_Diesel=request.form['Fuel_Type_Diesel']
    if(Fuel_Type_Diesel=='Diesel'):
              Fuel_Type_Petrol=0
              Fuel_Type_Diesel=1
    elif(Fuel_Type_Diesel=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
    else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
    Year=2020-Year
    Seller_Type_Individual=request.form['Seller_Type_Individual']
    if(Seller_Type_Individual=='Individual'):
         Seller_Type_Individual=1
    else:
         Seller_Type_Individual=0	
    Transmission_Manual=request.form['Transmission_Manual']
    if(Transmission_Manual=='Manual'):
            Transmission_Manual=1
    else:
            Transmission_Manual=0
    prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
    output=np.round(prediction[0],2)
    
    return render_template('index.html', prediction_text='Car can be sold at {} Rupees'.format(output))


if __name__ == "__main__":
    app.run(debug=True)