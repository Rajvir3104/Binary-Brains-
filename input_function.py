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


