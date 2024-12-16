import pandas as pd
import streamlit as st
from databasest import view_all_data


def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Student ID Number','Student Name','Address', 'Phone Number', 'Expiry date','Membership for a year'])
    with st.caption("View all Members Records"):
        st.dataframe(df)