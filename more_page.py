import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

@st.cache
def load_data():
    diabetes_dataset=pd.read_csv('diabetes.csv')
    return diabetes_dataset
def load_data1():
    heart_dataset=pd.read_csv('heart.csv')
    return heart_dataset
def load_data2():
    parkinson_dataset=pd.read_csv('parkinsons.csv')
    return parkinson_dataset

         


def show_more_page():
    st.title("Explore more page")

    st.write(
        """
    ### more info on data used to train the models and project documentations
    """
    )
    if st.button("View Diabetis Model Data Analysis"):
        st.subheader("Dataset Used To Train And Test The Model")

        

        result = load_data()
        
        with st.expander("View all Data Used To Train And Test The Diabetis Model"):
            st.dataframe(result)

        st.subheader("The Distribution Of The Labelled Data On The Dataset")
        with st.expander("View The Distribution Of The Labelled Data"):
            diabetis_df= result['Outcome'].value_counts().to_frame()
            diabetis_df = diabetis_df.reset_index()
            st.dataframe(diabetis_df)
            p1 = px.pie(diabetis_df,names='index',values='Outcome')
            st.plotly_chart(p1,use_container_width=True)
        st.subheader("The Distribution Of The Labelled Data On The Dataset Based On Age")
        with st.expander("View The Distribution Of The Labelled Data Based on Age"):
            data = result.groupby(["Age"])["Outcome"].mean().sort_values(ascending=True)
            st.bar_chart(data)

        st.subheader("The Distribution Of The Labelled Data On The Dataset Based On Blood Pressure")
        with st.expander("View The Distribution Of The Labelled Data Based on Blood Pressure"):

            data = result.groupby(["BloodPressure"])["Outcome"].mean().sort_values(ascending=True)
            st.line_chart(data)

    if st.button("View heart Disease Model Data Analysis"):
        st.subheader("Dataset Used To Train And Test The Model")

        

        result = load_data1()
        
        with st.expander("View all Data Used To Train And Test The Diabetis Model"):
            st.dataframe(result)

        st.subheader("The Distribution Of The Labelled Data On The Dataset")
        with st.expander("View The Distribution Of The Labelled Data"):
            heart_df= result['target'].value_counts().to_frame()
            heart_df = heart_df.reset_index()
            st.dataframe(heart_df)
            p1 = px.pie(heart_df,names='index',values='target')
            st.plotly_chart(p1,use_container_width=True)

        st.subheader("The Distribution Of The Labelled Data On The Dataset Based On Chest Pain Type")
        with st.expander("View The Distribution Of The Labelled Data Based on Chest Pain Type"):
            data = result.groupby(["cp"])["target"].mean().sort_values(ascending=True)
            st.bar_chart(data)

        st.subheader("The Distribution Of The Labelled Data On The Dataset Based On Age")
        with st.expander("View The Distribution Of The Labelled Data Based on Age"):

            data = result.groupby(["age"])["target"].mean().sort_values(ascending=True)
            st.line_chart(data)

    if st.button("View Parkinson's Disease Model Data Analysis"):
        st.subheader("Dataset Used To Train And Test The Model")

        

        result = load_data2()
        
        with st.expander("View all Data Used To Train And Test The Diabetis Model"):
            st.dataframe(result)

        st.subheader("The Distribution Of The Labelled Data On The Dataset")
        with st.expander("View The Distribution Of The Labelled Data"):
            parkinson_df= result['status'].value_counts().to_frame()
            parkinson_df = parkinson_df.reset_index()
            st.dataframe(parkinson_df)
            p1 = px.pie(parkinson_df,names='index',values='status')
            st.plotly_chart(p1,use_container_width=True)
        st.subheader("The Distribution Of The Labelled Data On The Dataset Based On MDVP:Jitter(Abs)")
        with st.expander("View The Distribution Of The Labelled Data Based on MDVP:Jitter(Abs)"):
            data = result.groupby(["MDVP:Jitter(Abs)"])["status"].mean().sort_values(ascending=True)
            st.bar_chart(data)

        st.subheader("The Distribution Of The Labelled Data On The Dataset Based On MDVP:Jitter(%)")
        with st.expander("View The Distribution Of The Labelled Data Based on Blood MDVP:Jitter(%)"):

            data = result.groupby(["MDVP:Jitter(%)"])["status"].mean().sort_values(ascending=True)
            st.line_chart(data)
    if st.button("View Project Documentation"):
        st.subheader("About This Project")
        with st.expander("View Project Documentation"):
            st.subheader("about the project")
            st.write("about the project")
            st.write("about the project")
        st.subheader("Disclaimer")
        with st.expander("View View Disclaimer Documentation"):
            st.subheader("project disclaimer")
            st.write("project disclaimer")
            st.write("project disclaimer")
        st.subheader("Terms And Conditions")
        with st.expander("View View Terms And Conditions Documentation"):
            st.subheader("project Terms And Conditions")
            st.write("project Terms And Conditions")
            st.write("project Terms And Conditions")
        
        
        

    

    