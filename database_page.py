from numpy import poly1d
import streamlit as st
import pandas as pd
# Data Viz Pkgs
import plotly.express as px 

from db_fxns import add_data, create_table, view_all_data, get_name, view_unique_name, edit_patient_data, delete_data, create_usertable, add_userdata, login_user




def show_database_page():
    st.title("Explore database page")

    st.write("You need to be logged in as qualified medical personnel to access database services.")
    st.sidebar.write("___________________________________________________________")
    authmenu = ["Login","Signup","Logout"]
    auth = st.sidebar.selectbox("Login or Signup or Logout",authmenu)
    
    if auth == "Login":
        st.sidebar.write(" # Login Here #")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password" ,type="password")
        if st.sidebar.checkbox("Login"):
            create_usertable()
            resultss = login_user(username,password)
            #if password == "1234":
            if resultss:
                st.success("Succesfully logged in as {}".format(username))
            

                st.write(
                    """
                ### more info on data used to train the model
                """
                )
                

                menu = ["Add New Patient Details","View All Patients Details","Update Patient Details","Delete Patient Details"]
                choice = st.selectbox("Menu",menu)
                create_table()

                if choice == "Add New Patient Details":
                    st.subheader("Add Patient Details")
                    col1,col2 = st.columns(2)
                    col3,col4,col5 = st.columns(3)
                    col6,col7 = st.columns(2)

                    with col1:
                        name = st.text_input("Patient's Full Name")
                    with col2:
                        id = st.text_input("Patient's ID Number")
                    with col3:
                        diabetis = st.selectbox("Diabetis Status" , ("Not Tested","Positive", "Negative"))
                    with col4:
                        heart = st.selectbox("Heart Disease Status" , ("Not Tested","Positive", "Negative"))
                    with col5:
                        parkinsons = st.selectbox("Parkinson's Disease  Status" , ("Not Tested","Positive", "Negative"))
                    with col6:
                        Hospital = st.text_input("Hosipital Name")
                    with col7:
                        date = st.date_input("Date of last testing")

                    add = st.button("Add Patient to database")
                    if add:
                        add_data(name,id,diabetis,heart,parkinsons,Hospital,date)
                        st.success("sucessfully added :: {} :: to database".format(name))
                elif choice == "View All Patients Details":
                    st.subheader("View Database")
                    result = view_all_data()
                    #st.write(result)
                    df = pd.DataFrame(result,columns=['Name of patient','ID Number.','Diabetis Status','Heart Status','Parkinsons Status','Hospital Name','Date of checking'])
                    with st.expander("View all Data"):
                        st.dataframe(df)
                    with st.expander("Diabetis Distribution  Summary"):
                        diabetis_df= df['Diabetis Status'].value_counts().to_frame()
                        diabetis_df = diabetis_df.reset_index()
                        st.dataframe(diabetis_df)
                        p1 = px.pie(diabetis_df,names='index',values='Diabetis Status')
                        st.plotly_chart(p1,use_container_width=True)

                        

                    with st.expander("heart Disease Distribution  Summary"):
                        heart_df= df['Heart Status'].value_counts().to_frame()
                        heart_df = heart_df.reset_index()
                        st.dataframe(heart_df)
                        p1 = px.pie(heart_df,names='index',values='Heart Status')
                        st.plotly_chart(p1,use_container_width=True)
                    with st.expander("Parkinson's Disease Distribution  Summary"):
                        parkinson_df= df['Parkinsons Status'].value_counts().to_frame()
                        parkinson_df = parkinson_df.reset_index()
                        st.dataframe(parkinson_df)
                        p1 = px.pie(parkinson_df,names='index',values='Parkinsons Status')
                        st.plotly_chart(p1,use_container_width=True)
                elif choice == "Update Patient Details":
                    st.subheader("Edit / Update Patient Details")
                    with st.expander("View Patient Current Data"):
                        result = view_all_data()
                        df = pd.DataFrame(result,columns=['Name of patient','ID Number.','Diabetis Status','Heart Status','Parkinsons Status','Hospital Name','Date of checking'])
                        st.dataframe(df)

                    list_of_name = [i [0] for i in view_unique_name()]
                    selected_name = st.selectbox("Patient's Detail To Edit",list_of_name)
                    selected_result = get_name(selected_name)

                    if selected_result:
                        

                        name = selected_result[0][0]
                        id = selected_result[0][1]
                        diabetis = selected_result[0][2]
                        heart = selected_result[0][3]
                        parkinsons = selected_result[0][4]
                        Hospital = selected_result[0][5]
                        date = selected_result[0][6]

                        col1,col2 = st.columns(2)
                        col3,col4,col5 = st.columns(3)
                        col6,col7 = st.columns(2)

                        
                        with col1:
                            new_name = st.text_input("Patient's Full Name",name)
                        with col2:
                            new_id = st.text_input("Patient's ID Number",id)
                        with col3:
                            new_diabetis = st.selectbox("Diabetis Status" , ["Not Tested","Positive", "Negative"])
                        with col4:
                            new_heart = st.selectbox("Heart Disease Status" , ["Not Tested","Positive", "Negative"])
                        with col5:
                            new_parkinsons = st.selectbox("Parkinson's Disease  Status" , ["Not Tested","Positive", "Negative"])
                        with col6:
                            new_Hospital = st.text_input("Hosipital Name",Hospital)
                        with col7:
                            new_date = st.date_input("Date of last testing")
                        
                    add = st.button("Update Patient details")
                    if add:
                        edit_patient_data(new_name,new_id,new_diabetis,new_heart,new_parkinsons,new_Hospital,new_date,name,id,diabetis,heart,parkinsons,Hospital,date)
                        st.success("sucessfully updated :: {} :: details to :: {} ".format(name,new_name))
                
                    with st.expander("View Patient Updated Data"):
                        result2 = view_all_data()
                        df2 = pd.DataFrame(result2,columns=['Name of patient','ID Number.','Diabetis Status','Heart Status','Parkinsons Status','Hospital Name','Date of checking'])
                        st.dataframe(df2)
                elif choice == "Delete Patient Details":
                    st.subheader("Delete Patient Details")
                    with st.expander("View Patient's Current Data"):
                        result = view_all_data()
                        df = pd.DataFrame(result,columns=['Name of patient','ID Number.','Diabetis Status','Heart Status','Parkinsons Status','Hospital Name','Date of checking'])
                        st.dataframe(df)

                    list_of_name = [i [0] for i in view_unique_name()]
                    selected_name = st.selectbox("Patient's Detail To Delete",list_of_name)
                    st.warning("Do You Want To Delete Patient :: {}  Details?".format(selected_name))
                    if st.button("Delete Patient's Details"):
                        delete_data(selected_name)
                        st.success("Patient Details Successfully deleted")
                    with st.expander("View Patient Updated Data"):
                        result3 = view_all_data()
                        df2 = pd.DataFrame(result3,columns=['Name of patient','ID Number.','Diabetis Status','Heart Status','Parkinsons Status','Hospital Name','Date of checking'])
                        st.dataframe(df2)
            else:
                st.warning("Incorrect Username/Password Combination")    
    elif auth == "Signup":
        st.sidebar.write(" # SignUp Here #")
        new_username = st.sidebar.text_input("User Name")
        new_email = st.sidebar.text_input("Email Address")
        new_regnumber = st.sidebar.text_input("Regestration Number")
        confirm_password = st.sidebar.text_input("Password" ,type="password")
        new_password = st.sidebar.text_input("Confirm Password" ,type="password")
        if st.sidebar.checkbox("SignUp"):
            if confirm_password == new_password:
                create_usertable()
                add_userdata(new_username,new_password,new_email,new_regnumber)
                st.success("Successfully Signed Up")
                st.info("Go to Login Tab to Login to the service")
            else:
                st.warning("SignUp Unsuccessful!")
                st.info("Make sure the passwords entered match each other")
    elif auth == "Logout":
        st.info("Successfully Logged out")
        st.write("You are currently logged out")