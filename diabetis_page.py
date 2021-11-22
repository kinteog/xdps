import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn import svm

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

classifiers = data["model"]

def show_diabetis_page():
    st.title("Diabetis Prediction Service")

    st.write("""### We need some information to predict Patient's Diabetis status""")

    Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=30, value=1, step=1)
    Glucose = st.number_input("Glucose", min_value=0, max_value=250, value=85, step=1)
    BloodPressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=66, step=1)
    SkinThickness = st.number_input("Skin Thickness", min_value=0, max_value=150, value=29, step=1)
    Insulin = st.number_input("Insulin Level", min_value=0, max_value=650, value=0, step=1)
    bmi = st.number_input("BMI value", min_value=0.0, max_value=50.0, value=26.6, step=0.1, format="%0f")
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0000, max_value=5.0000, value=0.03, step=0.01 , format="%0f")
    Agee = st.number_input("Age", min_value=0, max_value=150, value=31, step=1)

    ok = st.button("Predict diabetis status")
    if ok:
        diabetes_dataset=pd.read_csv('diabetes.csv')

        X = diabetes_dataset.drop(columns= 'Outcome' , axis=1)
        Y = diabetes_dataset['Outcome']

        scaler= StandardScaler()

        scaler.fit(X)

        standardized_data=scaler.transform(X)

        X = standardized_data
        Y = diabetes_dataset['Outcome']

        X_train,X_test,Y_train,Y_test=train_test_split(X,Y, test_size=0.2, stratify=Y , random_state=2)

        classifier=svm.SVC(kernel='linear')

        classifier.fit(X_train,Y_train)

        X_train_prediction=classifier.predict(X_train)

        training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

        X_test_prediction=classifier.predict(X_test)
        test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

        input_data =(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,bmi,DiabetesPedigreeFunction,Agee)

        input_data_as_numpy_array=np.asarray(input_data)
        #reshape the array as we are predicting for one instance

        input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
        
        std_data=scaler.transform(input_data_reshaped)

        prediction=classifiers.predict(std_data)

        if(prediction[0] ==0):
             st.subheader(f"The Patient is not Diabetic")
        else:
             st.subheader(f"The Patient is Diabetic")
        

        

       
    
    
