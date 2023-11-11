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

