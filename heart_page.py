import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_model():
    with open('saved_heart.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

classifiers = data["model"]

def show_heart_page():
    st.title("Heart Disease Prediction Service")

    st.write("""### We need some information to predict Patient's Heart Disease status""")

    age = st.number_input("Age of patient", min_value=0, max_value=150, value=10, step=1)
    gender = st.selectbox("Sex of patient" , ("Female","Male"))

    sex = 0 if gender == "Female" else 1
    
    cpselect = st.selectbox("Chest pain type" , ("Type 0","Type 1", "Type 2","Type 3"))

    ChestPain = 0 if cpselect == "Type 0" else 1 if cpselect == "Type 1"  else 2 if cpselect == "Type 2" else 3

    Restbp = st.number_input("Resting blood pressure (in mm Hg on admission to the hospital)", min_value=50, max_value=250, value=100, step=1)
    chol = st.number_input("serum cholestoral in mg/dl", min_value=100, max_value=700, value=100, step=1)
    fbsselect = st.selectbox("Fasting blood sugar & gt; 120 mg/dl", ("True","False"))

    fbs = 1 if fbsselect == "True" else 0

    electrocardiographic = st.number_input("resting electrocardiographic results", min_value=0.0, max_value=2.0, value=0.0, step=1.0 , format="%0f")
    heartrate = st.number_input("maximum heart rate achieved", min_value=0, max_value=300, value=0, step=1)
    anginaselect =st.selectbox("exercise induced angina",("Yes","No"))

    angina = 1 if anginaselect == "Yes" else 0

    oldpeak = st.number_input("ST depression induced by exercise relative to rest", min_value=0.0, max_value=10.0, value=1.0, step=0.1,format="%0f")
    slope = st.number_input("the slope of the peak exercise ST segment", min_value=0, max_value=2, value=0, step=1)
    ca = st.number_input("number of major vessels (0-3) colored by flourosopy", min_value=0, max_value=3, value=0, step=1)
    thal = st.number_input("thal: 3 = normal; 6 = fixed defect; 7 = reversable defect", min_value=0, max_value=8, value=0, step=1)
    st.write('<style>div.row-widget.stSelectbox>div{flex-direction:row;}</style>', unsafe_allow_html=True)

    ok = st.button("Predict heart disease status")
    if ok:
        # loading the csv data to a Pandas DataFrame
        heart_data = pd.read_csv('heart.csv')

        X = heart_data.drop(columns='target', axis=1)
        Y = heart_data['target']

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

        model = LogisticRegression()

        # training the LogisticRegression model with Training data
        model.fit(X_train, Y_train)

        # accuracy on training data
        X_train_prediction = model.predict(X_train)
        training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

        # accuracy on test data
        X_test_prediction = model.predict(X_test)
        test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

        input_data = (age,sex,ChestPain,Restbp,chol,fbs,electrocardiographic,heartrate,angina,oldpeak,slope,ca,thal)

        # change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data)

        # reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data_reshaped)
        print(prediction)

        if(prediction[0] ==0):
             st.subheader(f"The Person does not have a Heart Disease")
        else:
             st.subheader(f"The Person has Heart Disease")
        

        

       
    
    
