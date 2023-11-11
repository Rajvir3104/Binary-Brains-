import pandas as pd
import numpy as np
import statistics

""" 
A Module Defining all of the Functions used for the Hack the Change Reso

"""



def flight_emissions(num_flights):
    """
        Calculating the CO2 emissions per # of flight

        Parameters
        ----------
        
        Number of flights :int
        
            The Number of flights a user has in a years time (Tones of CO2)
        
    """
    
    flight = pd.read_csv(r"Data\AIRTRANS_CO2_11112023191907048.csv", low_memory =False)
    flight_can = flight[flight["LOCATION"] == "CAN"]
    flight_can = flight_can[flight_can["FREQUENCY"] == "A"]
    flight_can_passenger = flight_can[flight_can["Flight type"] == "Passenger flights"]


    flight_can_passenger = flight_can_passenger.groupby(['Time'])["Value"].mean().reset_index()

    passengers_by_year = [133426703,140892544,150808451,160641587,162864077,46349535]

    y =0
    emission_per_flight = []
    while y < 6:
        x = flight_can_passenger.iloc[y]
        x = x["Value"] / passengers_by_year[y]

        emission_per_flight.append(x)

        y+=1


    emission_per_flight = statistics.mean(emission_per_flight) * num_flights

    return(emission_per_flight)

def get_car_type():
    """
    This fucntion gets the input value for the type of car the user uses
    """
    # Define car types
    car_types = {
        1: 'Petrol Car',
        2: 'Hybrid Car',
        3: 'Electric Car',
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

def age_emissions(age):
    """
    The following data is the range of groups and average CO2 emissions
    per person, excluding transportation and travel. So basic needs and shelter 
    for the average person

    The keys are the upper limit of the age groups
    The values are tons of CO2 per year
    """
    ranges = {18: 3, 30: 7, 50: 10, 70: 9, 160: 7}

    for key, val in ranges.items():
        if age <= key:
            return val

    # If the age is greater than or equal to the largest key, return the value associated with it
    return ranges[max(ranges)]




    



