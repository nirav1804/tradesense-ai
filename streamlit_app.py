import streamlit as st
import pandas as pd
import os

st.title("📈 TradeSense AI")
st.subheader("Real-Time Trend Detection for BSE/NSE Stocks")

script_code = st.text_input("Enter BSE/NSE Script Code (e.g., RELIANCE):")
segment = st.selectbox("Select Segment", ["Cash", "Futures"])

if script_code:
    data_path = f"data/{script_code.upper()}.csv"
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        st.write(f"### Showing trend for: {script_code.upper()}")
        st.line_chart(df["Close"])
        st.write("**Trend:**", "Uptrend 📈" if df["Close"].iloc[-1] > df["Close"].iloc[0] else "Downtrend 📉")
    else:
        st.warning("No data found. Try again after the daily fetch.")
