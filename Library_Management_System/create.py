import streamlit as st
from database import add_data


def create():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        num = st.text_input("Book No")
        author = st.text_input("Author")
    with col2:
        title = st.text_input("Book Title")
        publisher = st.text_input("Publisher")
    with col3:
        genre = st.text_input("Genre")
        availability = st.selectbox("Availability",["Yes","No","Not supplying anymore"])
    with col4:
        des = st.text_input("mini description")
        copies = st.number_input("Number of copies")    


    if st.button("Add this book to the library"):
        add_data(num,title,genre,des,author,publisher,availability,copies)
        st.success("Successfully added the book: {}".format(title))
