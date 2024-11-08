import streamlit as st

st.title("ACTL3182 Course Project - Data Visualisation Tool")
st.subheader("Created by Tom Coates | z5420082 | November 2024")
st.write("This project centred around the creation of two investment portfolios. Our investment universe was based on London Stock Exchange (LSE) listed stocks. "
         "Our portfolio objectives were as follows:")
st.write("""
1. **Index Tracking Portfolio:** The objective of this portfolio was to replicate the performance of the FTSE 100 Index while only being able to invest in 20-30 stocks. Short-selling
constraints were also imposed and we were required to be fully invested, meaning that we would not hold cash. 
2. **Capital Growth Portfolio:**  This is a speculative portfolio which aims to demonstrate excess growth above that of the growth of the FTSE 100 Index. The view of this portfolio 
is to maximise capital gains over the investment horizon. Both fundamental and technical analysis was employed for stock selection when it came to this portfolio.""")
st.write("The investment horizon of the portfolio ran from the 16th of September 2024 ending on the 18th of October 2024.")
st.write("Data was aggregated from Yahoo Finance and FactSet for use in both screening and testing our strategies.")
