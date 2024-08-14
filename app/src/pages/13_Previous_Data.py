import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests
import os

SideBarLinks()

st.write("# View 10 Most Expensive and 10 Least Expensive Homes")

# Base URL for user data
base_url = 'http://localhost:4000/u/users'

# Display all users
database_name = os.getenv('DB_NAME')  

url = 'http://localhost:4000/l/listings'

try:
    response = requests.get(url)
    if response.status_code == 200:
        all_data = response.json()
    else:
        st.error(f"Failed to retrieve all listings. Status code: {response.status_code}")
        st.text("Response:" + response.text)
except requests.exceptions.RequestException as e:
    st.error("An error occurred while trying to connect to the API to fetch all users:")
    st.text(str(e))

url = 'http://localhost:4000/l/tenLeastExpensive'
try:
    response = requests.get(url)
    if response.status_code == 200:
        all_data = response.json()
        st.write("ten least expensive listings:")
        st.dataframe(all_data)  # Displaying all user data in a dataframe
    else:
        st.error(f"Failed to retrieve all listings. Status code: {response.status_code}")
        st.text("Response:" + response.text)
except requests.exceptions.RequestException as e:
    st.error("An error occurred while trying to connect to the API to fetch all users:")
    st.text(str(e))


url = 'http://localhost:4000/l/tenMostExpensive'
try:
    response = requests.get(url)
    if response.status_code == 200:
        all_data = response.json()
        st.write("ten most expensive listings:")
        st.dataframe(all_data)  # Displaying all user data in a dataframe
    else:
        st.error(f"Failed to retrieve all listings. Status code: {response.status_code}")
        st.text("Response:" + response.text)
except requests.exceptions.RequestException as e:
    st.error("An error occurred while trying to connect to the API to fetch all users:")
    st.text(str(e))

url = 'http://localhost:4000/l/getPriceChanges'

# Conditionally make API request based on user input for specific user details
try:
    response = requests.get(url)
    if response.status_code == 200:
        user_data = pd.DataFrame(response.json())
        user_data.set_index('Street', inplace=True)
        st.line_chart(user_data[['Current Price', 'Predicted Future Price', 'Previous Price']])  # Displaying specific user data in JSON format for clarity
    else:
        st.error(f"Failed to retrieve data for listing ID {listing_id}. Status code: {response.status_code}")
        st.text("Response:" + response.text)
except requests.exceptions.RequestException as e:
    st.error(f"An error occurred while trying to connect to the API to fetch listing ID {listing_id}:")
    st.text(str(e))
