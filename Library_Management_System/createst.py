import streamlit as st
from databasest import add_data


def create():
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["id", "sname", "address","phone","expiry","mem"])
    with tab1:
        st.header("Enter the student ID number")
        sid = st.text_input("Student ID Number")
    with tab2:
        st.header("Enter Student Name")
        sname = st.text_input("Student Name")
    with tab3:
        st.header("Student address")
        address = st.text_input("Address")
    with tab4:
        st.header("Phone Number")
        phone = st.number_input("Phone Number")
    with tab5:
        st.header("Expiry date")
        expiry = st.date_input("Membership Expiry Date")
    with tab6:
        st.header("Check the below options")
        mem = st.radio("1 year membership",["Yes","No"])

    
    if st.button("Add this student as a member"):
        add_data(sid,sname,address,phone,expiry,mem)
        st.success("Successfully added member: {}".format(sname))
