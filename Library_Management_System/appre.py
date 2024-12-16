import streamlit as st
from createre import create
from databasere import create_table
from deletere import delete
from readre import read
from updatere import update

def main():
    st.title("Book Borrow Report")
    menu = ["Generate Report", "View all reports", "Extend date", "Delete report"]
    choice = st.sidebar.radio("Here is the list of operations you can perform", menu)

    create_table()
    if choice == "Generate Report":
        st.subheader("Enter report details:")
        create()

    elif choice == "View all reports":
        st.subheader("View present reports")
        read()

    elif choice == "Extend date":
        st.subheader("Extend date")
        update()

    elif choice == "Delete report":
        st.subheader("Book has been returned")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
