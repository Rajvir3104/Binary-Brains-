import Functions as fn
from Functions import user

my_instance = user()


import stats


def total_emissions():
    age = int(
        input("Enter your age: ")
    )  # base it off of calories needed for average person that age
    flights_per_year = int(input("Enter number of flights per year: "))
    daily_drive_km = float(input("Enter average daily kilonmeters driven: "))
    car_type = my_instance.get_car_type()

    travel_km_values = {"Petrol Car": 0.17, "Hybrid Car": 0.068, "Electric Car": 0.047}
    co2_car = (
        travel_km_values[car_type] * daily_drive_km * 365
    ) / 1000  # the co2 is in kg

    co2_flight = fn.flight_emissions(flights_per_year)
    co2_age = fn.age_emissions(age)
    co2_clothing=fn.clothing_emissions
    # Add flight c02 calculations here

    total = co2_car + co2_flight + co2_age +co2_clothing # converting to tons
    return total


total = my_instance.total_emissions()


print(f"Your total emissions for a year is: {total:.0f} Tons of CO2")
sus_score = stats.point_system(total, stats.average_carbon_canada)
print(f"The average scroe is 50 and your sustainability score is: {sus_score}")
