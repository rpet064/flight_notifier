from notification_manager import NotificationManager
import pandas as pd
from csv_manager import CSVManager
from countryinfo import CountryInfo
from flight_data import FlightData


def api_handler():
    name = input("Welcome to the flight notifier. What's your name?")
    file_name = f"{name}_flight_details.csv"
    # check if CSV exists
    try:
        pd.read_csv(file_name)
    except FileNotFoundError:
        country_name = input(f"Hi {name}, What country are you from?")
        pod = input("What city would you like to depart from?")
        destinations = input(
            "What cities would you like to go to? Please separate cities like so: (Tokyo, New York, London)")
        country = CountryInfo(country_name)
        currency_array = country.currencies()
        currency = currency_array[0]
        # module inputs user data into CSV
        CSVManager(pod, name, destinations, country_name, file_name)
    finally:
        # call flight APIs
        fd = FlightData(file_name)
        fd.find_pod()
        fd.find_poa()
        data = fd.flight_search()
    return data


def data_handler(data2):
    flight_price = 100000
    for index in range(len(data2["data"])):
        for key in data2["data"][0:len(data2["data"])]:
            # finds the cheapest flight
            if flight_price > key["price"]:
                # stores information from cheapest flight
                flight_price = key["price"]
                fly_from = key["flyFrom"]
                fly_to = key["flyTo"]
                bags_price = key["bags_price"]["1"]
                availability = key["availability"]["seats"]
                departure_time = key["local_departure"]
                booking_link = key["deep_link"]

    departure_time = departure_time.split("T")[0]
    # fixes grammar bug for seat and seats
    if availability == 1 or 0:
        seat = "seat"
    else:
        seat = "seats"
    # nm = NotificationManager()
    # # sends a text message using information from flight API
    # nm.message_sender(message=f'''The cheapest flight from {fly_from} to {fly_to} in the next 3 months is ${flight_price}.
    # It leaves on {departure_time}. Check in luggage is ${bags_price}.
    # You better get in quick, there are only {availability} {seat} available.
    # Please click on this link if you are interested in booking {booking_link}
    # ''')

data_handler(api_handler())