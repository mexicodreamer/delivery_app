
import streamlit as st
import sqlite3

connection = sqlite3.connect("taxi.db", check_same_thread = False)
cursor = connection.cursor()

def formCreation():
    st.write("Please fill in this form")
    with st.form(key = "Registration Form"):
        name = st.text_input("Enter name: ")
        phone = st.text_input("Enter phone: ")
        email = st.text_input("Enter email: ")
        submit = st.form_submit_button(label="Register")

    if submit == True:
        st.success("Registration was successfull")
        addInfo(name,phone,email)

def addInfo(a,b,c):
    cursor.execute( '''
CREATE TABLE IF NOT EXISTS registrations(
    NAME TEXT(50)
    PHONE TEXT(50)
    EMAIL TEXT(50)
    ) '''
    )

    cursor.execute("INSERT INTO registrations VALUES (?,?,?)", (a,b,c))

    connection.commit()
    connection.close()
    st.success("User has been added to the SQLite database")

formCreation()


    
