import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBRegressor

st.set_page_config(page_title="AirBnB Price Predictor in New York City", page_icon=":house:", layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>Predicting Airbnb Prices in New York City</h1>", unsafe_allow_html=True)

st.sidebar.header("Enter Airbnb Details")

def user_input():
    latitude = st.sidebar.number_input('Latitude', 40.499790, 40.913060, 40.755942, step=1e-7, format="%.6f")
    longitude = st.sidebar.number_input('Longitude', -74.244420	, -73.712990, -73.977619, step=1e-7, format="%.6f")
    availability_365 = st.sidebar.number_input('Number of days available per year', 1, 365, 24)
    minimum_nights = st.sidebar.number_input('Minimum nights of stay', 1, 12, 2)
    calculated_host_listings_count = st.sidebar.number_input('calculated_host_listings_count', 1, 327, 6)
    reviews_per_month = st.sidebar.number_input('Reviews per month', 0, 58,5)
    number_of_reviews = st.sidebar.number_input('Number of reviews', 0,629,4)
    neighbourhood_popularity = st.sidebar.number_input('Neighbourhood popularity', 0.00,10.00,1.43)
    dummy_Bronx = st.sidebar.selectbox('Bronx', (0, 1))
    dummy_Brooklyn = st.sidebar.selectbox('Brooklyn', (0, 1))
    dummy_Manhattan = st.sidebar.selectbox('Manhattan', (0, 1))
    dummy_Queens = st.sidebar.selectbox('Queens', (0, 1))
    dummy_Staten_Island = st.sidebar.selectbox('Staten Island', (0, 1))
    dummy_Entire_home_apt = st.sidebar.selectbox('Entire Home / Appartment', (0, 1))
    dummy_Private_room = st.sidebar.selectbox('Private Room', (0, 1))
    dummy_Shared_room = st.sidebar.selectbox('Share Room', (0, 1))
    distance_to_wall_street = st.sidebar.number_input('Distance to Manhattan', 0, 31, 23)
    txt2 = st.sidebar.subheader("Does your listing contain the following words ?")
    nyc = st.sidebar.selectbox('NYC', (0, 1))
    near = st.sidebar.selectbox('Near ', (0, 1))
    heights = st.sidebar.selectbox('Heights', (0, 1))
    spacious = st.sidebar.selectbox('Spacious', (0, 1))
    brownstone = st.sidebar.selectbox('Brownstone', (0, 1))
    bed = st.sidebar.selectbox('Bed', (0, 1))
    square = st.sidebar.selectbox('Square', (0, 1))
    huge = st.sidebar.selectbox('Huge', (0, 1))
    heart = st.sidebar.selectbox('Heart', (0, 1))
    bushwick = st.sidebar.selectbox('Bushwick', (0, 1))
    neighbourhood = st.sidebar.number_input('Neighbourhood', 0, 6, 4)

    data = {'latitude':latitude,
            'longitude':longitude,
            'availability_365': availability_365,
            'minimum_nights': minimum_nights,
            'calculated_host_listings_count': calculated_host_listings_count,
            'reviews_per_month': reviews_per_month,
            'number_of_reviews': number_of_reviews,
            'neighbourhood_popularity' : neighbourhood_popularity,
            'dummy_Bronx': dummy_Bronx,
            'dummy_Brooklyn': dummy_Brooklyn,
            'dummy_Manhattan': dummy_Manhattan,
            'dummy_Queens': dummy_Queens,
            'dummy_Staten_Island': dummy_Staten_Island,
            'dummy_Entire_home_apt':  dummy_Entire_home_apt,
            'dummy_Private_room': dummy_Private_room,
            'dummy_Shared_room': dummy_Shared_room,
            'distance_to_wall_street': distance_to_wall_street,
            'nyc' : nyc,
            'near' : near,
            'heights': heights,
            'spacious': spacious,
            'brownstone': brownstone,
            'bed': bed,
            'square': square,
            'huge' : huge,
            'heart': heart,
            'bushwick' : bushwick,
            'neighbourhood': neighbourhood
    }
    appt_parametre = pd.DataFrame(data,index=[0])
    return appt_parametre


df = user_input()


model = XGBRegressor()
model.load_model("/Users/Koko/Desktop/finalized_model7.json")
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






