import streamlit as st
from create import create
from database import create_table
from delete import delete
from read import read
from update import update

def main():
    st.title("Library Management System")
    menu = ["Add Books", "View Books", "Edit Books", "Remove Books"]
    choice = st.sidebar.radio("Menu", menu)

    create_table()
    if choice == "Add Books":
        st.subheader("Enter Book Details:")
        create()

    elif choice == "View Books":
        st.subheader("View created records")
        read()

    elif choice == "Edit Books":
        st.subheader("Update created records")
        update()

    elif choice == "Remove Books":
        st.subheader("Delete created records")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
