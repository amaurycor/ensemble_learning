import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBRegressor

st.set_page_config(page_title="AirBnB Price Predictor in New York City", page_icon=":house:", layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>Predicting Airbnb Prices in New York City</h1>", unsafe_allow_html=True)

st.sidebar.header("Enter your Airbnb Details")

def user_input():
    txt1 = st.sidebar.subheader("Enter location")
    latitude = st.sidebar.number_input('Latitude', 40.499790, 40.913060, 40.755942, step=1e-7, format="%.6f")
    longitude = st.sidebar.number_input('Longitude', -74.244420	, -73.712990, -73.977619, step=1e-7, format="%.6f")
    availability_365 = st.sidebar.number_input('Number of days available per year', 1, 365, 24)
    minimum_nights = st.sidebar.number_input('What is the minimum number of days a visitor must reserve for your listing ?', 1, 12, 2)
    host_activity = st.sidebar.number_input('How many active listings do you have ?', 0, 629, 4)
    reviews_per_month = st.sidebar.number_input('How many reviews per month do your listing receive ?', 0, 58, 5)
    number_of_reviews = st.sidebar.number_input('In total, how many reviews does your listing have? ', 0, 629, 4)
    time_since_last_review = st.sidebar.number_input('When was your last reviews (in days) ?', 0, 4000, 50)
    #neighbourhood_popularity = st.sidebar.selectbox('Neighbourhood popularity', 0.00, 10.00, 1.43)
    txt2 = st.sidebar.subheader("Choose 1 if your listing is located in one of these boroughs (leave 0 for others)")
    dummy_Bronx = st.sidebar.selectbox('Bronx', (0, 1))
    dummy_Brooklyn = st.sidebar.selectbox('Brooklyn', (0, 1))
    dummy_Manhattan = st.sidebar.selectbox('Manhattan', (0, 1))
    dummy_Queens = st.sidebar.selectbox('Queens', (0, 1))
    dummy_Staten_Island = st.sidebar.selectbox('Staten Island', (0, 1))
    txt3 = st.sidebar.subheader("Choose 1 if your listing is one of the following (leave 0 for others) : ")
    dummy_Entire_home_apt = st.sidebar.selectbox('Entire Home / Appartment', (0, 1))
    dummy_Private_room = st.sidebar.selectbox('Private Room', (0, 1))
    dummy_Shared_room = st.sidebar.selectbox('Share Room', (0, 1))
    txt4 = st.sidebar.subheader("How far (in kilometers) is your listing from : ?")
    distance_to_wall_street = st.sidebar.number_input('Wall Street', 0, 31, 23)
    distance_to_closest_station = st.sidebar.number_input('Closest Metro Station', 0, 31, 23)

    data = {'latitude':latitude,
            'longitude':longitude,
            'availability_365': availability_365,
            'minimum_nights': minimum_nights,
            'host_activity':  host_activity,
            'reviews_per_month': reviews_per_month,
            'number_of_reviews': number_of_reviews,
            'time_since_last_review': time_since_last_review,
            #'neighbourhood_popularity': neighbourhood_popularity,
            'dummy_Bronx': dummy_Bronx,
            'dummy_Brooklyn': dummy_Brooklyn,
            'dummy_Manhattan': dummy_Manhattan,
            'dummy_Queens': dummy_Queens,
            'dummy_Staten_Island': dummy_Staten_Island,
            'dummy_Entire_home_apt':  dummy_Entire_home_apt,
            'dummy_Private_room': dummy_Private_room,
            'dummy_Shared_room': dummy_Shared_room,
            'distance_to_wall_street': distance_to_wall_street,
            'distance_to_closest_station': distance_to_closest_station
    }
    appt_parametre = pd.DataFrame(data,index=[0])
    return appt_parametre


df = user_input()


model = XGBRegressor()
model.load_model("/Users/Koko/Desktop/xg_boost6.json")
y_pred = model.predict(df)

price = round(np.exp(y_pred[0]))

st.caption("<h1 style='text-align: center; color: white;'>Price Per Night</h1>", unsafe_allow_html=True)


m2 = st.metric("", "$"+f"{price:,}")
css='''
[data-testid="metric-container"] {
    width: fit-content;
    margin: auto;
}

[data-testid=m2] > div {
    width: fit-content;
    margin: auto;
}

[data-testid="metric-container"] label {
    width: fit-content;
    margin: auto;
}
'''

st.markdown(f'<style>{css}</style>',unsafe_allow_html=True)

st.subheader("Property Location")
st.map(df)






