import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

def load_model():
    with open('saved_park.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

classifiers = data["model"]

def show_parkinson_page():
    st.title("Parkinson's disease Prediction Service")

    st.write("""### We need some information to predict Patient's Parkinson's disease status""")


    st.write("""### Several measures of variation in fundamental frequency""")

    MDVPFoHz = st.number_input("MDVP:Fo(Hz) - Average vocal fundamental frequency", min_value=50.0, max_value=300.0, value=100.1, step=1.0, format="%0f")
    MDVPFhiHz = st.number_input("MDVP:Fhi(Hz) - Maximum vocal fundamental frequency", min_value=100.0, max_value=600.0, value=100.1, step=1.0, format="%0f")
    MDVPFloHz = st.number_input("MDVP:Flo(Hz) - Minimum vocal fundamental frequency", min_value=60.0, max_value=250.0, value=100.1, step=1.0, format="%0f")
    MDVPJitterPercent = st.number_input("MDVP:Jitter(%)", value=0.1, step=1.0, format="%0f")
    MDVPJitterAbs = st.number_input("MDVP:Jitter(Abs)",  max_value=1.0, value=0.1, step=0.1, format="%0f")
    MDVPRAP = st.number_input("MDVP:RAP",  max_value=1.0, value=0.1, step=0.1, format="%0f")
    MDVPPPQ = st.number_input("MDVP:PPQ",  max_value=1.0, value=0.1, step=0.1 , format="%0f")

    st.write("""### Several measures of variation in amplitude""")

    JitterDDP = st.number_input("Jitter:DDP",  max_value=1.0, value=0.1, step=1.0, format="%0f")
    MDVPShimmer = st.number_input("MDVP:Shimmer", max_value=1.0, value=0.1, step=0.1, format="%0f")
    MDVPShimmerdB = st.number_input("MDVP:Shimmer(dB)", max_value=2.0, value=1.0, step=0.1, format="%0f")
    ShimmerAPQ3 = st.number_input("Shimmer:APQ3", max_value=1.0, value=0.1, step=0.1, format="%0f")
    ShimmerAPQ5 = st.number_input("Shimmer:APQ5", max_value=1.0, value=0.1, step=0.1, format="%0f")
    MDVPAPQ = st.number_input("MDVP:APQ", max_value=1.0, value=0.1, step=0.1, format="%0f")
    ShimmerDDA = st.number_input("Shimmer:DDA", max_value=1.0, value=0.1, step=0.1, format="%0f")

    st.write("""### Two measures of ratio of noise to tonal components in the voice""")

    NHR = st.number_input("NHR",  max_value=1.0, value=0.1, step=0.1, format="%0f")
    HNR = st.number_input("HNR", max_value=40.0, value=10.1, step=0.1, format="%0f")

    st.write("""### Two nonlinear dynamical complexity measures""")

    RPDE = st.number_input("RPDE", max_value=1.0, value=0.1, step=0.1, format="%0f")
    D2 = st.number_input("D2",min_value=0.0, max_value=1.0, value=0.1, step=0.1, format="%0f")

    st.write("""### Signal fractal scaling exponent""")

    DFA = st.number_input("DFA",  max_value=1.0, value=0.1, step=0.1, format="%0f")

    st.write("""### Three nonlinear measures of fundamental frequency variation""")

    spread1 = st.number_input("spread1",  max_value=1.0, value=0.1, step=0.1, format="%0f")
    spread2 = st.number_input("spread2", max_value=5.0, value=0.1, step=0.1, format="%0f")
    PPE = st.number_input("PPE", max_value=1.0, value=0.1, step=0.1 , format="%0f")






    ok = st.button("Predict parkinson's status")
    if ok:
        # loading the data from csv file to a Pandas DataFrame
        parkinsons_data = pd.read_csv('parkinsons.csv')

        X = parkinsons_data.drop(columns=['name','status'], axis=1)
        Y = parkinsons_data['status']

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

        scaler = StandardScaler()

        scaler.fit(X_train)

        X_train = scaler.transform(X_train)

        X_test = scaler.transform(X_test)

        model = svm.SVC(kernel='linear')

        # training the SVM model with training data
        model.fit(X_train, Y_train)

        X_train_prediction = model.predict(X_train)
        training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

       
        # accuracy score on training data
        X_test_prediction = model.predict(X_test)
        test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

        input_data = (MDVPFoHz,MDVPFhiHz, MDVPFloHz,MDVPJitterPercent,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdB,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,D2,DFA,spread1,spread2,PPE)

        # changing input data to a numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the numpy array
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        # standardize the data
        std_data = scaler.transform(input_data_reshaped)

        prediction = model.predict(std_data)
        print(prediction)
        if(prediction[0] ==0):
             st.subheader(f"The Person does not have Parkinsons Disease")
        else:
             st.subheader(f"The Person has Parkinsons")
        

        

       
    
    
