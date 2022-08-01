import requests
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask,request, render_template,redirect,url_for 
import os
from werkzeug.utils import secure_filename
from tensorflow.python.keras.backend import set_session
app=Flask(__name__)
model=load_model("vegetable.h5")
model1=load_model("fruit.h5")
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction')
def prediction():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])


def predict():
    if request.method=='POST':
        f=request.files['image']
        basepath=os.path.dirname(__file__)
        file_path=os.path.join(
            basepath,'uploads',secure_filename(f.filename))
        f.save(file_path)
        img=image.load_img(file_path,target_size=(128,128))
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        plant=request.form['plant']
        print(plant)
        preds=model.predict(x)
        print(preds)
        test = " ".join([str(item) for item in preds])
        #return test
        if(plant=="fruit"): 
            y = np.argmax(model.predict(x),axis=1)
            index  = ['Apple___Black_rot','Apple___healthy','Corn_(maize)___Northern_Leaf_Blight','Corn_(maize)___healthy','Peach___Bacterial_spot','Peach___healthy']
            df=pd.read_excel('precautions - fruits.xlsx')
            text = df.iloc[y[0]]['caution']
            print(df.iloc[y[0]]['caution'])
            print(text)
        else:
            y = np.argmax(model1.predict(x),axis=1)
            index  = ['Pepper,_bell___Bacterial_spot','Pepper,_bell___healthy','Potato___Early_blight','Potato___healthy','Potato___Late_blight','Tomato___Bacterial_spot','Tomato___Late_blight','Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot']
            df=pd.read_excel('precautions - veg.xlsx')
            text = df.iloc[y[0]]['caution']
            print(text)
        return render_template('predict.html',mytext=text, mypath=file_path)
        # if(plant=="vegetable"):
        #      preds=model.predict(x)
        #      print(preds)
        #      df=pd.read_excel('precautions - veg.xlsx')
        #      print(df.iloc[preds[0]]['caution'])
        # else:
        #     preds=model1.predict(x)
        #     df=pd.read_excel('precautions - fruits.xlsx')
        #     print(df.ilolc[preds[0]]['caution'])
        # return df.iloc[preds[0]]['caution']

# =============================================================================
# if __name__=="__main__":
#      app.run(debug=False)
# =============================================================================


if __name__=="__main__":
     app.run(debug=True)
     from flask import Flask
     app = Flask(__name__)
