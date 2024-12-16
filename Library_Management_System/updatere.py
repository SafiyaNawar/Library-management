import datetime
import pandas as pd
import streamlit as st
from databasere import view_all_data, view_only_repnum, get_repnum, edit_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Report number','Student name','Book number','student id', 'issue date', 'return date'])
    with st.caption("Current reports"):
        st.dataframe(df)
    list_of_studs = [i[0] for i in view_only_repnum()]
    selected_stud = st.selectbox("report date to extend", list_of_studs)
    selected_result = get_repnum(selected_stud)
    if selected_result:
        repnum = selected_result[0][0]
        sname = selected_result[0][1]
        bnum = selected_result[0][2]
        sid = selected_result[0][3]
        issued = selected_result[0][4]
        returnd = selected_result[0][5]
        

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["repnum","sname", "bnum", "sid","issued","returnd"])
    with tab1:
        st.header("Report number")
        nrepnum = st.number_input("report number",repnum)
    with tab2:
        st.header("Borrower name")
        nsname = st.text_input("Student name",sname)
    with tab3:
        st.header("book number")
        nbnum = st.number_input("book number",bnum)
    with tab4:
        st.header("student id number")
        nsid = st.number_input("stud id",sid)
    with tab5:
        st.header("issue date")
        nissued = st.date_input("issued on",issued)
    with tab6:
        st.header("return date")
        nreturnd = st.date_input("returned by",returnd)
        

        if st.button("Update report Details"):
            edit_data(nrepnum,nsname,nbnum,nsid,nissued,nreturnd,repnum,sname,bnum,sid,issued,returnd)
            st.success("Successfully updated report :: {} to ::{}".format(returnd,nreturnd))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Report number','Student name','Book number','student id', 'issue date', 'return date'])
    with st.expander("Updated data"):
        st.dataframe(df2)
