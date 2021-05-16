import streamlit as st
from datetime import date, datetime
import requests

### Page configuration

st.set_page_config(layout='wide')

### Container ( Header )

container_ = st.beta_container()

### Side bar

st.sidebar.markdown(f"""# Request for a taxi in NY """)

pickup_date = st.sidebar.date_input("",date.today())
pickup_time = st.sidebar.time_input('At which time do you want the pick up?', datetime.now())

st.sidebar.markdown(f"""
    ## How many passengers?
    """)

passenger_count = st.sidebar.slider('', 1, 5, 1)

pickup_datetime = f"{pickup_date} {pickup_time} UTC"

### Central container structured by columns

cols = st.beta_columns(3)

cols[0].markdown(f"""
    ## Pick up coordinates
    """)

pickup_latitude = cols[0].number_input('Pick up latitude',value=40.75)
pickup_longitude = cols[0].number_input('Pick up longitude',value=-73.98)

cols[1].markdown(f"""
    ## Drop off coordinates
    """)

dropoff_latitude = cols[1].number_input('Drop off latitude',value=40.70)
dropoff_longitude = cols[1].number_input('Drop off longitude',value=-73.90)

### Bottom line to call for prediction and show API call parameters
    
params_ = {"key":"2013-07-06 17:18:00.000000000",
            "pickup_datetime": pickup_datetime,
            "pickup_longitude": pickup_longitude,
            "pickup_latitude": pickup_latitude,
            "dropoff_longitude": dropoff_longitude,
            "dropoff_latitude": dropoff_latitude,
            "passenger_count": int(passenger_count)
            }

if st.button(f'Predict taxi fare'):
    # URL_API_ = "https://taxifareapi-mmmvoa6ccq-ew.a.run.app/predict_fare"
    URL_API_ = "https://taxifare.lewagon.ai/predict_fare"
    res_ = requests.get(URL_API_, params=params_).json()
    cols[2].markdown(f"""
                    ## Predicted taxi fare
                    """)
    cols[2].markdown(f"# **{round(res_['prediction'],2)} $**")

with st.beta_expander("See API parameters"):
    st.json(params_)

### Write it in the container ( Header )

with container_:

    date_ = pickup_date.strftime("%d-%b-%Y")
    time_ = pickup_time.strftime("%H:%M")

    st.markdown(f"## **Taxi fare predicion for {passenger_count} passenger(s) on {date_} at {time_}**")

    st.markdown("*-> Number of passengers and/or pickup information can be changed using the side bar *")



