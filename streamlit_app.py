import streamlit as st
import pandas as pd
import requests
import snowflake.connector

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

# request the data
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")

# normalize the json output
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Put the data in a DF and let streamlit display it
st.dataframe(fruityvice_normalized)


# New Section to display fruitvice API response
st.header("Fruitvice Fruit Advice!")
fruit_choice = st.text_input("What fruit would you like information about?", "Kiwi")
st.write("The user entered", fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# display user's choice in DF
user_fruitchoice = pd.json_normalize(fruityvice_response.json())
st.dataframe(user_fruitchoice)


# Test our new snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchone()
st.text("The fruit load list contains:")
st.text(my_data_row)
