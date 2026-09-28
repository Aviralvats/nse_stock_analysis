import streamlit as st
import pandas as pd

from function import market_overview


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="NSE Stock Analysis",
    page_icon="📊",
    layout="wide"
)


# ---------------- DATA ----------------

df25 = pd.read_csv(
    "BhavCopy_NSE_CM_0_0_0_20260925_F_0000.csv"
)


# ---------------- HEADER ----------------

st.title("📊 NSE Market Dashboard")
st.caption("Market overview • 25 September 2026")

if st.button("🚀 Back to Home"):
    st.switch_page("Home.py")

st.divider()


# ---------------- MARKET OVERVIEW ----------------

st.header("Market Overview")

(
    total_txn,
    total_volume,
    total_trf,
    fig,
    top_return,
    bottom_return,
    advancing,
    declining,
    unchanged,
    company,
    volume,
    volume2,
    volume3,
    trf_highest,
    company_txn,
    stocks,
    candle_figs,
    pie_fig
) = market_overview(df25)


# ---------------- KPI CARDS ----------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Transactions",
    f"{total_txn:,}"
)

col2.metric(
    "Total Trading Volume",
    f"{total_volume:,}"
)

col3.metric(
    "Total Traded Value",
    f"₹{total_trf:,.0f}"
)


# ---------------- MARKET ACTIVITY ----------------

st.header("Market Activity")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Companies by Trading Volume")
    st.pyplot(fig, use_container_width=True)

with col2:
    st.subheader("Market Breadth")
    st.pyplot(pie_fig, use_container_width=True)


# ---------------- MARKET PERFORMANCE ----------------

st.header("Market Performance")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚀 Top 10 Returns")

    st.dataframe(
        top_return,
        use_container_width=True,
        hide_index=True
    )

with col2:
    st.subheader("📉 Lowest 10 Returns")

    st.dataframe(
        bottom_return,
        use_container_width=True,
        hide_index=True
    )


# ---------------- MARKET BREADTH ----------------

st.header("Market Breadth")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🟢 Advancing",
    f"{advancing:,}"
)

col2.metric(
    "🔴 Declining",
    f"{declining:,}"
)

col3.metric(
    "⚪ Unchanged",
    f"{unchanged:,}"
)


# ---------------- TOP COMPANIES ----------------

st.header("Market Leaders")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Highest Trading Volume")
    st.write(f"**{company}**")
    st.caption(f"Volume: {volume:,}")

with col2:
    st.subheader("🔄 Highest Transactions")
    st.write(f"**{company_txn}**")
    st.caption(f"Transactions: {volume2:,}")

with col3:
    st.subheader("💰 Highest Traded Value")
    st.write(f"**{trf_highest}**")
    st.caption(f"Value: ₹{volume3:,.0f}")


# ---------------- STOCK ANALYSIS ----------------

st.header("Stock Analysis")

selected_company = st.selectbox(
    "Select a stock",
    stocks
)

st.plotly_chart(
    candle_figs[selected_company],
    use_container_width=True
)