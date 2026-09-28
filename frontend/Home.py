import streamlit as st

st.set_page_config(
    page_title="NSE Stock Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 NSE Stock Analysis")
st.header("Explore NSE market data and statistics")
st.subheader("Select Date")
year = st.selectbox(
    "Select Year",
    ["24-9-26", "25-9-26"]
)
if st.button("🚀 EXPLORE MARKET"):
    if year == "24-9-26":
        st.switch_page("pages/market_24.py")
    else:
        st.switch_page("pages/market_25.py")
st.write("Welcome to the NSE Stock Analysis application! This app provides insights and visualizations for stock data from the National Stock Exchange (NSE).")
st.header('Prediction')
st.subheader('Analyse potential next day movements using ml')
if st.button("🚀 Predictions"):
    st.switch_page("pages/predictions.py")
