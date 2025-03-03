import pickle
import streamlit as st
import pandas as pd

from Prepro import Prepro
from MissingValueImputer import MissingValueImputer
from RareLabelTransformer import RareLabelTransformer
from Remove import Remove

filename = 'Beta16CModel.sav'
model = pickle.load(open(filename, 'rb'))


def main():
    st.title('Hostreamlittel Booking Cancelation Analysis')

    hotel = st.selectbox("Hotel", ["Resort Hotel", "City Hotel"])
    lead_time = st.number_input("Lead Time", value=342)
    arrival_date_year = st.number_input("Arrival Date Year", value=2015)
    arrival_date_month = st.selectbox("Arrival Date Month", [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ], index=6)  # Default to July
    arrival_date_day_of_month = st.number_input("Arrival Date Day of Month", value=1)
    stays_in_weekend_nights = st.number_input("Stays in Weekend Nights", value=0)
    stays_in_week_nights = st.number_input("Stays in Week Nights", value=0)
    adults = st.number_input("Adults", value=2)
    children = st.number_input("Children", value=0)
    babies = st.number_input("Babies", value=0)
    meal = st.selectbox("Meal", ["BB", "HB", "FB", "SC"])  # Default to BB
    country = st.text_input("Country", value="PRT")
    market_segment = st.selectbox("Market Segment", [
        "Direct", "Corporate", "Online TA", "Offline TA/TO", "Complementary", "Groups"
    ], index=0)  # Default to Direct
    distribution_channel = st.selectbox("Distribution Channel", [
        "Direct", "Corporate", "TA/TO", "GDS"
    ], index=0)
    is_repeated_guest = st.radio("Is Repeated Guest", ["No", "Yes"], index=0)
    previous_cancellations = st.number_input("Previous Cancellations", value=0)
    previous_bookings_not_canceled = st.number_input("Previous Bookings Not Canceled", value=0)
    reserved_room_type = st.text_input("Reserved Room Type", value="C")
    assigned_room_type = st.text_input("Assigned Room Type", value="C")
    booking_changes = st.number_input("Booking Changes", value=3)
    deposit_type = st.selectbox("Deposit Type", ["No Deposit", "Non Refund", "Refundable"], index=0)  # Default to No Deposit
    agent = st.number_input("Agent", value=304)
    days_in_waiting_list = st.number_input("Days in Waiting List", value=0)
    customer_type = st.selectbox("Customer Type", [
        "Transient", "Contract", "Transient-Party", "Group"
    ], index=0)  # Default to Transient
    required_car_parking_spaces = st.number_input("Required Car Parking Spaces", value=0)
    total_of_special_requests = st.number_input("Total of Special Requests", value=0)

    if st.button('Submit'):
        is_repeated_guest_value = 1 if is_repeated_guest == "Yes" else 0

        list_features = ['hotel', 'lead_time', 'arrival_date_year', 'arrival_date_month', 
                 'arrival_date_day_of_month', 'stays_in_weekend_nights', 'stays_in_week_nights', 
                 'adults', 'children', 'babies', 'meal', 'country', 'market_segment', 
                 'distribution_channel', 'is_repeated_guest', 'previous_cancellations', 
                 'previous_bookings_not_canceled', 'reserved_room_type', 'assigned_room_type', 
                 'booking_changes', 'deposit_type', 'agent', 'days_in_waiting_list', 
                 'customer_type', 'required_car_parking_spaces', 'total_of_special_requests']
                
        row = [
            hotel,  # hotel
            lead_time,  # lead_time
            arrival_date_year,  # arrival_date_year
            arrival_date_month,  # arrival_date_month
            arrival_date_day_of_month,  # arrival_date_day_of_month
            stays_in_weekend_nights,  # stays_in_weekend_nights
            stays_in_week_nights,  # stays_in_week_nights
            adults,  # adults
            children,  # children
            babies,  # babies
            meal,  # meal
            country,  # country
            market_segment,  # market_segment
            distribution_channel,  # distribution_channel
            is_repeated_guest_value,  # is_repeated_guest
            previous_cancellations,  # previous_cancellations
            previous_bookings_not_canceled,  # previous_bookings_not_canceled
            reserved_room_type,  # reserved_room_type
            assigned_room_type,  # assigned_room_type
            booking_changes,  # booking_changes
            deposit_type,  # deposit_type
            agent,  # agent
            days_in_waiting_list,  # days_in_waiting_list
            customer_type,  # customer_type
            required_car_parking_spaces,  # required_car_parking_spaces
            total_of_special_requests,  # total_of_special_requests
        ]

        input_data = pd.DataFrame([row], columns=list_features)
        makePrediction = model.predict(input_data)
        output = makePrediction[0]

        st.success('The customer will cancel' if output ==
                   1 else 'The customer will not cancel')


if __name__ == '__main__':
    main()
