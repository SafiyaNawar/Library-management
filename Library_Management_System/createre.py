import streamlit as st
from databasere import add_data
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Safiyasql@13",
    database="lib"
)
c = mydb.cursor()

def create():
    tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["repnum","sname", "bnum", "sid","issued","returnd"])
    with tab1:
        st.header("Report number")
        repnum = st.text_input("report num")
    with tab2:
        st.header("Borrower name")
        sname = st.text_input("Student name")
    with tab3:
        st.header("book number")
        bnum = st.number_input("book number")
    with tab4:
        st.header("student id number")
        sid = st.number_input("stud id")
    with tab5:
        st.header("issue date")
        issued = st.date_input("issued on")
    with tab6:
        st.header("return date")
        returnd = st.date_input("returned by")
        
    if st.button("Generate report"):
        add_data(repnum,sname,bnum,sid,issued,returnd)
        #if c.excecute("SELECT copies from books" == 0):
         #   st.warning("No copies left")

       # c.execute("UPDATE books SET `copies` = `copies`- 1 WHERE bnum=%s",(bnum))
        st.success("Successfully generated report for book: {}".format(bnum))
