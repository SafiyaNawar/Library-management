import datetime
import pandas as pd
import streamlit as st
from databasest import view_all_data, view_only_sid, get_sid, edit_stud_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Student ID Number','Student Name','Address', 'Phone Number', 'Expiry date','Membership for a year'])
    with st.caption("Current Students"):
        st.dataframe(df)
    list_of_studs = [i[0] for i in view_only_sid()]
    selected_stud = st.selectbox("Student details to Edit", list_of_studs)
    selected_result = get_sid(selected_stud)
    if selected_result:
        sid = selected_result[0][0]
        sname = selected_result[0][1]
        address = selected_result[0][2]
        phone = selected_result[0][3]
        expiry = selected_result[0][4]
        mem = selected_result[0][5]


    col1, col2, col3 = st.columns(3)
    with col1:
        sid = st.text_input("Student ID Number",sid)
        phone = st.number_input("Phone Number",phone)
    with col2:
        sname = st.text_input("Student Name",sname)
        expiry = st.date_input("Membership Expiry Date",expiry)
    with col3:
        address = st.text_input("Address",address)
        mem = st.selectbox("1 year membership",["Yes","No"])


        if st.button("Update Student Details"):
            edit_stud_data(nsid,nsname,naddress,nphone,nexpiry,nmem,sid,sname,address,phone,expiry,mem)
            st.success("Successfully updated details for student:: {} to ::{}".format(name,nname))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Student ID Number','Student Name','Address', 'Phone Number', 'Expiry date','Membership for a year'])
    with st.expander("Updated data"):
        st.dataframe(df2)
