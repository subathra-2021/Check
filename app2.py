# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 10:50:21 2022

@author: drng
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:32:18 2022

@author: drng
"""

# import requests
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.models import load_model
# import numpy as np
# import pandas as pd
# import tensorflow as tf
from flask import Flask,request, render_template,redirect,url_for 
# import os
# from werkzeug.utils import secure_filename
# from tensorflow.python.keras.backend import set_session
app=Flask(__name__)
# model=load_model("vegetable.h5")
# model1=load_model("fruit.h5")

@app.route('/')
def home():
    return render_template('index.html')
#@app.route('/prediction')

# # def prediction():
# #     return render_template('predict.html')
# # @app.route('/predict',methods=['POST'])
if __name__ == "__main__":
    app.run(debug=True)
     