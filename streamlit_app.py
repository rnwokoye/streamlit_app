import streamlit as st
import pandas as pd
import requests

st.title("New Healthy Diner")


st.header("Breakfast Favorites")

st.text("🥣 Omega 3 & Blueberry Oatmea")
st.text("🥗 Kale, Spinach & Rocket Smoothi")
st.text("🐔 Hard-Boiled Free-Range Eg")
st.text("🥑🍞 Avocado Toa")

st.header("🍌🥭 Build Your Own Fruit Smoothie 🍇")

my_fruit_list = pd.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
).set_index("Fruit")


# Fruit list here
fruits_selected = st.multiselect(
    "Pick some fruits for yourself:",
    list(my_fruit_list.index),
    ["Avocado", "Strawberries"],
)

# fruits to show
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
# st.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)

# New section to display fruity vice api response
st.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())
