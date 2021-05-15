import streamlit as st
from datetime import date, datetime
import requests

'''
# Taxi fare prediction challenge
## From where to where ?
'''

st.sidebar.markdown(f"""
    # Request for a taxi in NY 

    ## When and how many passengers?
    """)

URL_API_ = "https://taxifareapi-mmmvoa6ccq-ew.a.run.app/predict_fare"
# URL_API_ = "https://taxifare.lewagon.ai/predict_fare"

pickup_date = st.sidebar.date_input("When do you need the taxi?",date.today())
pickup_time = st.sidebar.time_input('At which time do you want the pick up?', datetime.now())
passenger_count = st.sidebar.slider('How many passengers?', 1, 5, 1)

pickup_datetime = f"{pickup_date} {pickup_time} UTC"

# pickup_latitude=40.7482
# pickup_longitude=-73.985
# dropoff_latitude=40.7699
# dropoff_longitude=-73.9752

cols = st.beta_columns(2)

pickup_latitude = cols[0].st.number_input('Pickup latitude',40.7482)
pickup_longitude = cols[0].st.number_input('Pickup longitude',-73.985)
dropoff_latitude = cols[1].st.number_input('Dropoff latitude',40.7482)
dropoff_longitude = cols[1].st.number_input('Dropoff longitude',-73.9752)
    
params_ = {"key":["2013-07-06 17:18:00.000000000"],
            "pickup_datetime": [pickup_datetime],
            "pickup_longitude": [pickup_longitude],
            "pickup_latitude": [pickup_latitude],
            "dropoff_longitude": [dropoff_longitude],
            "dropoff_latitude": [dropoff_latitude],
            "passenger_count": [int(passenger_count)]
            }

if st.button('Predict taxi fare',):
    res_ = requests.get(URL_API_, params=params_).json()
    st.write(f"Taxi fare prediction is {round(res_['prediction'],2)} $")

if st.checkbox('Show params'):
    params_

