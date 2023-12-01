import streamlit as st

st.title("Weather Forecast for the next days  ")
place = st.text_input("Place:")
days = st.slider("Forecast days", min_value=1, max_value=5, help="number of days", key='slider')
option = st.selectbox("Select data to view", ('Temperature', 'Climate'))
st.subheader(f"{option} for the next {days} days in {place}")