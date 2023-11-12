import pandas as pd
import numpy as np
import statistics

""" 
A Module Defining all of the Functions used for the Hack the Change Reso

"""


class user:
    def __init__(self):
        """
        Initialize the angle and initial velocity of the projectile

        Parameters
        ----------


        """

    def flight_emissions(number_of_flight):
        """
        Calculating the CO2 emissions per # of flight

        Parameters
        ----------

        Number of flights :int

            The Number of flights a user has in a years time (Tones of CO2)

        """

        flight = pd.read_csv(
            r"C:\Users\ashle\Documents\ENGG year 2\Binary-Brains-\Data\AIRTRANS_CO2_11112023191907048.csv"
        )
        flight_can = flight[flight["LOCATION"] == "CAN"]
        flight_can = flight_can[flight_can["FREQUENCY"] == "A"]
        flight_can_passenger = flight_can[
            flight_can["Flight type"] == "Passenger flights"
        ]

        flight_can_passenger = (
            flight_can_passenger.groupby(["Time"])["Value"].mean().reset_index()
        )

        passengers_by_year = [
            133426703,
            140892544,
            150808451,
            160641587,
            162864077,
            46349535,
        ]

        y = 0
        emission_per_flight = []
        while y < 6:
            x = flight_can_passenger.iloc[y]
            x = x["Value"] / passengers_by_year[y]

            emission_per_flight.append(x)

            y += 1

        emission_per_flight = statistics.mean(emission_per_flight) * number_of_flight

        return emission_per_flight

    def get_car_type(self):
        """
        This fucntion gets the input value for the type of car the user uses
        """
        # Define car types
        car_types = {
            1: "Petrol Car",
            2: "Hybrid Car",
            3: "Electric Car",
        }

        # Display menu
        print("Choose the type of car you own:")
        for key, value in car_types.items():
            print(f"{key}: {value}")

        user_choice = int(input("Enter the code for your car type: "))

        if user_choice in car_types:
            car_type = car_types[user_choice]
            print(f"You selected: {car_type}")
        else:
            print("Invalid choice. Please select a valid car type.")
        return car_type

    def total_emissions(self):
        # age = int(input("Enter your age: ")) #base it off of calories needed for average person that age
        flights_per_year = int(input("Enter number of flights per year: "))
        daily_drive_km = float(input("Enter average daily kilonmeters driven: "))
        car_type = self.get_car_type()  # fix this

        travel_km_values = {
            "Petrol Car": 0.17,
            "Hybrid Car": 0.068,
            "Electric Car": 0.047,
        }
        co2_car = travel_km_values[car_type] * daily_drive_km * 365  # the co2 is in kg

        co2_flight = flights_per_year * 100000000
        
        co2_age = 100000000
        
        # Add flight c02 calculations here

        total = (co2_car + co2_flight + co2_age) / 20000000  # converting to tons
        return total
        
    def calculate_annual_co2_emissions():


        CO2_PER_ITEM = {
            "shoes": 0.0136078,
            "shirts": 0.006117828,
            "hoodies": 0.0136078,
            "jeans":0.022,
            "jackets": 0.07002,}
        
        def calculate_emissions(item, quantity):
            item_emission = CO2_PER_ITEM.get(item)* quantity
            return item_emission
        
        emission = 0
        for item in CO2_PER_ITEM:
            quantity = print(float(input("How many %s do you buy per year?".format(item))))
            emission = calculate_emissions(item,quantity) + emission

    #     # print("Where do you usually buy %s".format(item))
    #     # for shop in SHOP_LOCATIONS:
    #     #     print(shop)
    #     # location = print(input())

        print("Your total CO2 emissions from buying clothing: {:.2f} tonnes per year".format(emission))
