import streamlit as st
from datetime import date, datetime
import requests

st.set_page_config(layout='wide')

'''
# Taxi fare prediction challenge
## From where to where ?
'''

URL_API_ = "https://taxifareapi-mmmvoa6ccq-ew.a.run.app/predict_fare"
# URL_API_ = "https://taxifare.lewagon.ai/predict_fare"

cols = st.beta_columns(3)

st.sidebar.markdown(f"""
    # Request for a taxi in NY 

    ## When do you need a taxi ?
    """)

pickup_date = st.sidebar.date_input("",date.today())
pickup_time = st.sidebar.time_input('At which time do you want the pick up?', datetime.now())

st.sidebar.markdown(f"""
    ## How many passengers?
    """)

passenger_count = st.sidebar.slider('', 1, 5, 1)

pickup_datetime = f"{pickup_date} {pickup_time} UTC"

# pickup_latitude=40.7482
# pickup_longitude=-73.985
# dropoff_latitude=40.7699
# dropoff_longitude=-73.9752

cols[0].markdown(f"""
    ## Pick up
    """)

pickup_latitude = cols[0].number_input('Pick up latitude',40.7482)
pickup_longitude = cols[0].number_input('Pick up longitude',-73.985)

cols[1].markdown(f"""
    ## Drop off
    """)

dropoff_latitude = cols[1].number_input('Drop off latitude',40.7482)
dropoff_longitude = cols[1].number_input('Drop off longitude',-73.9752)
    
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
    cols[2].markdown(f"""
                    ## Predicted taxi fare
                    """)
    cols[2].write(f"{round(res_['prediction'],2)} $")

if st.checkbox('Show params'):
    st.write(params_)

