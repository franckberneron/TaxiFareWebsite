from urllib import request
import streamlit as st
import requests as rq
import datetime as dt


url = 'https://taxifare.lewagon.ai/predict'

'''
# Easily find out your NYC taxifare !
'''

with st.form("Enter data to calculate your fare:"):

    pickup_date         = st.date_input('your pickup day:', dt.date(2012, 12, 1))
    pickup_time         = st.time_input('your pickup time:', dt.time(11, 0))
    pickup_datetime     = f'{pickup_date} {pickup_time}'
    pickup_longitude    = st.number_input('your pickup long:', value=40.7614327)
    pickup_latitude     = st.number_input('your pickup lat:', value=-73.9798156)
    dropoff_longitude   = st.number_input('your dropoff long:', value=40.6413111)
    dropoff_latitude    = st.number_input('your dropoff lat:', value=-73.7803331)
    passenger_count     = st.number_input('How many passengers:', min_value=1, max_value=8, step=1, value=1)

    submitted = st.form_submit_button("Calculate")
    if submitted:
        params = dict(
            pickup_datetime     = pickup_datetime,
            pickup_longitude    = pickup_longitude,
            pickup_latitude     = pickup_latitude,
            dropoff_longitude   = dropoff_longitude,
            dropoff_latitude    = dropoff_latitude,
            passenger_count     = passenger_count
        )

        res = rq.get(url, params)
        fare = int(res.json()['fare'])

        #st.info(res.json())

        st.title(f"Your fare is {fare} USD")
