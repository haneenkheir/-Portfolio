def hotel_cost(num_nights):
    return 50 * num_nights
    
def plane_cost(city):
    if city.lower() == 'london':
        return 50 
    elif city.lower() == 'paris':
        return 40 
    elif city.lower() == 'new york':
        return 60
    else: 
        print("Invalid city choice.")

def car_rental(rental_days):
    return 10 * rental_days 

def holiday_cost(city_flight, num_nights, rental_days):
    hotel = hotel_cost(num_nights)
    flight = plane_cost(city_flight)
    car = car_rental(rental_days)
    
    total_cost = hotel + flight + car
    
    print("Hotel Cost:", hotel)
    print("Flight Cost:", flight)
    print("Car Rental Cost:", car)
    
    return total_cost

# Get user input, while loop added to account for errors
while True:
    print("City options: London, New York, Paris")
    city_flight = input("Which city from the above list will you be flying to: ").lower()
    if city_flight in ['london', 'new york', 'paris']:
        break
    else:
        print("Invalid city choice. Please try again.")

while True:
    try:
        num_nights = int(input("How many nights are you staying: "))
        if num_nights > 0:
            break
        else:
            print("Invalid number of nights. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number of nights.")

while True:
    try:
        rental_days = int(input("How many days will you hire a car for: "))
        if rental_days > 0:
            break
        else:
            print("Invalid number of rental days. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")

# Calculate and display the holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)
print("The total cost of your holiday is:", total_cost)