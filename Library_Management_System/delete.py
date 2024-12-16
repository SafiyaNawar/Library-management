import pandas as pd
import streamlit as st
from database import view_all_data, view_only_title, delete_data


def delete():
    st.title("Delete any book that you are taking off the library")
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Book no','Book Title','Genre', 'Description', 'Author','Publisher', 'Availability', 'copies'])
    with st.caption("Current books"):
        st.dataframe(df)

    list_of_books = [i[0] for i in view_only_title()]
    selected_book = st.selectbox("Book to Delete", list_of_books)
    st.warning("Do you want to delete book::{}".format(selected_book))
    if st.button("Delete Book"):
        delete_data(selected_book)
        st.success("Book has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Book no','Book Title','Genre', 'Description', 'Author','Publisher', 'Availability', 'copies'])
    with st.expander("Updated data"):
        st.dataframe(df2)