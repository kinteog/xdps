import streamlit as st
from PIL import Image
from heart_page import show_heart_page
from diabetis_page import show_diabetis_page
from parkinson_page import show_parkinson_page
from more_page import show_more_page

img = Image.open('test.jpg')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden; }
        </style>

"""
st.set_page_config(page_title='Disease Prediction System', page_icon=img)
#st.set_page_config(page_title='Disease Prediction System', page_icon=":shark:")
st.markdown(hide_menu_style, unsafe_allow_html=True)


page = st.sidebar.selectbox("Choose The disease you want to predict", ("Heart", "Diabetis", "Parkinson", "More"))

if page == "Heart":
    show_heart_page()
elif page  == "Diabetis":
    show_diabetis_page()
elif page  == "Parkinson":
    show_parkinson_page()
else:
    show_more_page()