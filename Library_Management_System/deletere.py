import pandas as pd
import streamlit as st
from databasere import view_all_data, view_only_repnum, delete_data


def delete():
    st.title("Delete report when book returned")
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Report Number','Student name','Book number','student id', 'issue date', 'return date'])
    with st.caption("Current reports"):
        st.dataframe(df)

    list_of_studs = [i[0] for i in view_only_repnum()]
    selected_stud = st.selectbox("report to Delete", list_of_studs)
    st.warning("Has the book been returned::{}".format(selected_stud))
    if st.button("Delete report"):
        delete_data(selected_stud)
        st.success("report deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Report Number','Student name','Book number','student id', 'issue date', 'return date'])
    with st.caption("Updated data"):
        st.dataframe(df2)