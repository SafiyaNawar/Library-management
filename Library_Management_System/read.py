import pandas as pd
import streamlit as st
from database import view_all_data


def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Book no','Book Title','Genre', 'Description', 'Author','Publisher', 'Availability', 'copies'])
    with st.caption("View all Book Records"):
        st.dataframe(df)