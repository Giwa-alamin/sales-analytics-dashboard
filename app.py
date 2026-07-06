import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Analytics Dashboard")

df = pd.read_csv("sales_data.csv")

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

st.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")
st.metric("Total Orders", len(df))
st.metric("Customers", df["Customer"].nunique())

st.dataframe(df)
