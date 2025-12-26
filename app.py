import streamlit as st
import pandas as pd
import plotly.express as px

# عنوان صفحه
st.title("داشبورد شاخص اثرات اقلیم کویری استان یزد")

# خواندن داده
df = pd.read_csv("desert_climate_yazd.csv",encoding="utf-8-sig")

# فیلترها
city = st.selectbox("انتخاب شهرستان", df["شهرستان"].unique())
month = st.selectbox("انتخاب ماه", df["ماه"].unique())

# فیلتر داده‌ها
filtered = df[(df["شهرستان"] == city) & (df["ماه"] == month)]

# نمایش شاخص
st.metric(
    "میانگین شاخص اثرات اقلیم کویری (°C)",
    round(filtered["میانگین_دما"].mean(), 1)
)

# نمودار
fig = px.line(
    filtered,
    x="ماه",
    y="میانگین_دما",
    markers=True,
    title=f"روند تغییرات میانگین دما در شهرستان",
    labels={
        "day": "روز",
        "desert_climate_index": "شاخص اثرات اقلیم کویری (°C)"
    }
)

st.plotly_chart(fig)

# جدول داده‌ها
st.subheader("داده‌های روزانه")

st.dataframe(filtered)

save working version







