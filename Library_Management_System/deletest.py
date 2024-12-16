import pandas as pd
import streamlit as st
from databasest import view_all_data, view_only_sid, delete_data


def delete():
    st.title("Delete any student whose membership expired")
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Student ID Number','Student Name','Address', 'Phone Number', 'Expiry date','Membership for a year'])
    with st.caption("Current members"):
        st.dataframe(df)

    list_of_studs = [i[0] for i in view_only_sid()]
    selected_stud = st.selectbox("Member to Delete", list_of_studs)
    st.warning("Do you want to delete member::{}".format(selected_stud))
    if st.button("Delete Member"):
        delete_data(selected_stud)
        st.success("Member has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Student ID Number','Student Name','Address', 'Phone Number', 'Expiry date','Membership for a year'])
    with st.caption("Updated data"):
        st.dataframe(df2)