import Functions as FN

user = FN.user

total = user.total_emissions()
print(f"Your total emissions for a year is: {total} Tons CO2")

def total_emissions():
    age = int(input("Enter your age: ")) #base it off of calories needed for average person that age 
    flights_per_year = int(input("Enter number of flights per year: "))
    daily_drive_km = float(input("Enter average daily kilonmeters driven: "))
    car_type = get_car_type()

    travel_km_values = { "Petrol Car":0.17, "Hybrid Car":0.068, "Electric Car": 0.047}
    co2_car = travel_km_values[car_type] * daily_drive_km * 365 #the co2 is in kg

    co2_flight = flights_per_year * 100000000
    co2_age = 100000000
    # Add flight c02 calculations here

    total = (co2_car + co2_flight + co2_age)/1000 #converting to tons
    return total
