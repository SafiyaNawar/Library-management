import pandas as pd
import streamlit as st
from databasere import view_all_data


def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Report number','Student name','Book number','student id', 'issue date', 'return date'])
    with st.caption("View all Reports"):
        st.dataframe(df)