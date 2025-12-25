import streamlit as st
import pandas as pd
import plotly.express as px

# عنوان صفحه
st.title("داشبورد شاخص اثرات اقلیم کویری استان یزد")

# خواندن داده
df = pd.read_csv("./desert_climate_yazd.csv")

# فیلترها
city = st.selectbox("انتخاب شهرستان", df["city"].unique())
month = st.selectbox("انتخاب ماه", df["month"].unique())

# فیلتر داده‌ها
filtered = df[(df["city"] == city) & (df["month"] == month)]

# نمایش شاخص
st.metric(
    "میانگین شاخص اثرات اقلیم کویری (°C)",
    round(filtered["desert_climate_index"].mean(), 1)
)

# نمودار
fig = px.line(
    filtered,
    x="day",
    y="desert_climate_index",
    markers=True,
    title="روند روزانه شاخص اثرات اقلیم کویری",
    labels={
        "day": "روز",
        "desert_climate_index": "شاخص اثرات اقلیم کویری (°C)"
    }
)

st.plotly_chart(fig)

# جدول داده‌ها
st.subheader("داده‌های روزانه")

st.dataframe(filtered)
