import streamlit as st
from PIL import Image
from heart_page import show_heart_page
from diabetis_page import show_diabetes_page
from parkinson_page import show_parkinson_page
from more_page import show_more_page
from database_page import show_database_page



img = Image.open('images/Main.png')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden; }
        </style>

"""
st.set_page_config(page_title='Disease Prediction System', page_icon=img)
#st.set_page_config(page_title='Disease Prediction System', page_icon=":shark:")
st.markdown(hide_menu_style, unsafe_allow_html=True)


page = st.sidebar.selectbox("Choose The disease you want to predict", ( "Home", "Diabetes", "Heart", "Parkinson", "More"))

if page == "Heart":
    show_heart_page()
elif page  == "Diabetes":
    show_diabetes_page()
elif page  == "Parkinson":
    show_parkinson_page()
elif page  == "Home":
    show_database_page()
else:
    show_more_page()