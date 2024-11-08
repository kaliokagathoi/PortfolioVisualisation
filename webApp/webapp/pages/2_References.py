import streamlit as st
import pandas as pd

st.title("Data Sources - from Submitted Markdown Scripts and Yahoo Finance")
df = pd.read_csv("C:/Users/tomco/OneDrive - UNSW/2024/ACTL3182/Assignment/webApp/webappdata.csv", parse_dates=['Date'], index_col='Date')
df.index = df.index.date
st.dataframe(df)

st.write('Index Tracking Portfolio - Currency Hedged: ITP_H')
st.write('Index Tracking Portfolio - Currency Un-Hedged: ITP_UH')
st.write('Capital Growth Portfolio - Currency Hedged: CGP_H')
st.write('Capital Growth Portfolio - Currency Un-Hedged: CGP_UH')
st.write('FTSE 100 Index - Currency Hedged: FTSE_H')
st.write('FTSE 100 Index - Currency Un-Hedged: FTSE_UH')