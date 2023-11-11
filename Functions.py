import pandas as pd
import numpy as np
import statistics

""" 
A Module Defining all of the Functions used for the Hack the Change Reso

"""

class user:

    def __init__(self, num_flights):
        """
            Initialize the angle and initial velocity of the projectile
            
            Parameters
            ----------
            
            num_flights: intiger

                The Number of flights that a user takes on an annual basis
                
            """
        
        self.num_flights = num_flights

    def flight_emissions(number_of_flight):
        """
            Calculating the CO2 emissions per # of flight

            Parameters
            ----------
            
            Number of flights :int
            
                The Number of flights a user has in a years time (Tones of CO2)
            
        """
        
        flight = pd.read_csv(r"C:\Users\ashle\Documents\ENGG year 2\Binary-Brains-\Data\AIRTRANS_CO2_11112023191907048.csv")
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


        emission_per_flight = statistics.mean(emission_per_flight) * number_of_flight

        return(emission_per_flight)




