import datetime
import pandas as pd
import streamlit as st
from database import view_all_data, view_only_title, get_title, edit_book_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Book no','Book Title','Genre', 'Description', 'Author','Publisher', 'Availability', 'copies'])
    with st.caption("Current Books"):
        st.dataframe(df)
    list_of_books = [i[0] for i in view_only_title()]
    selected_book = st.selectbox("Book details to Edit", list_of_books)
    selected_result = get_title(selected_book)
    if selected_result:
        num = selected_result[0][0]
        title = selected_result[0][1]
        genre = selected_result[0][2]
        des = selected_result[0][3]
        author = selected_result[0][4]
        publisher = selected_result[0][5]
        availability = selected_result[0][6]
        copies = selected_result[0][7]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        nnum = st.text_input("Books No", num)
        nauthor = st.text_input("Author", author)
    with col2:
        ntitle = st.text_input("Book Title", title)
        npublisher = st.text_input("Publisher", publisher)
    with col3:
        ngenre = st.text_input("Genre", genre)
        navailability = st.selectbox("Availability",["Yes","No","Not suppyling anymore"])
    with col4:
        ndes = st.text_input("mini description", des)
        ncopies = st.number_input("Number of copies", copies)



        if st.button("Update Book Details"):
            edit_book_data(nnum,ntitle,ngenre,ndes,nauthor,npublisher,navailability,ncopies, num,title,genre,des,author,publisher,availability,copies)
            st.success("Successfully updated values for book:: {} to ::{}".format(title, ntitle))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Book no','Book Title','Genre', 'Description', 'Author','Publisher', 'Availability', 'copies'])
    with st.expander("Updated data"):
        st.dataframe(df2)
