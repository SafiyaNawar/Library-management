import streamlit as st
from createst import create
from databasest import create_table
from deletest import delete
from readst import read
from updatest import update

def main():
    st.title("Student Membership Details")
    menu = ["Add Member", "View all members", "Edit members", "Remove members"]
    choice = st.sidebar.radio("Here is the list of operations you can perform", menu)

    create_table()
    if choice == "Add Member":
        st.subheader("Enter student Details:")
        create()

    elif choice == "View all members":
        st.header("View added records")
        read()

    elif choice == "Edit members":
        st.subheader("Update added records")
        update()

    elif choice == "Remove members":
        st.subheader("Delete added records")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
