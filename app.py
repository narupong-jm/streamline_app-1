import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("⛳️ My first app!")

placeholder = st.empty()
status = st.radio("Select an option.", ["Success", "Error"], index=None)

if status == "Success":
    placeholder.success("Success!")
else:
    placeholder.error("Error!!!")

st.write("Hello again! Awesome!")
st.info("This is a information.")
st.success("This is coll!")
st.error("This is an error message.")
st.warning("This is a warning.")

st.header("Area Chart")
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.area_chart(chart_data)

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

c = (
    alt.Chart(df).mark_circle(size=60).encode(
        x='bill_length_mm',
        y='body_mass_g',
        color='species',
        tooltip=['island', 'sex']
    ).interactive()
)
st.header("Scatter Chart")
st.altair_chart(c, use_container_width=True)
