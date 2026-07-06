import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Analytics Dashboard")

df = pd.read_csv("sales_data.csv")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Sidebar
st.sidebar.header("Filters")

category = st.sidebar.multiselect(
    "Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[df["Category"].isin(category)]

# KPIs
revenue = filtered_df["Revenue"].sum()
orders = len(filtered_df)
customers = filtered_df["Customer"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Revenue", f"${revenue:,.2f}")
col2.metric("Orders", orders)
col3.metric("Customers", customers)

st.divider()

# Charts
left, right = st.columns(2)

with left:
    fig = px.bar(
        filtered_df,
        x="Product",
        y="Revenue",
        color="Category",
        title="Revenue by Product"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig2 = px.pie(
        filtered_df,
        names="Category",
        values="Revenue",
        title="Revenue by Category"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

fig3 = px.line(
    filtered_df,
    x="Date",
    y="Revenue",
    markers=True,
    title="Revenue Trend"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Sales Data")

st.dataframe(filtered_df, use_container_width=True)
