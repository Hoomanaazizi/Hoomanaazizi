# first we should define a function to find out the cost of hotel?
def hotel_cost(x, y):
    total = x * y
    return total

num_nights = int(input("how many nights are you planning to stay? "))
price_per_night = float(input("how much you will be charged per night? "))

print(hotel_cost(num_nights, price_per_night))

#second we should find the car rental cost
def car_rental(x, y):
    total = x * y
    return total

rental_cost_per_day = float(input("how much is car retnal price per day? "))
rental_days = int(input("how many days you are planning to rent the car for? "))

print(car_rental(rental_cost_per_day, rental_days))


# make a library for ticket prices
Available_tickets_price = {
    "Tokyo": 1579,
    "Bangkok": 1823,
    "Seoul": 1227
}

# ... your code for hotel and car rental calculations ...

# Ticket price dictionary
available_ticket_prices = {
    "Tokyo": 1579,
    "Bangkok": 1823,
    "Seoul": 1227
}

# Get user input for flight destination with validation
# while True:
#     flight_price = input("Please select one of these destinations (Tokyo, Bangkok, Seoul): ")
#     flight_price = flight_price.lower()  # Convert to lowercase for case-insensitive matching

#     if flight_price in available_ticket_prices:
#         break
#     else:
#         print("Invalid destination. Please select from the available options.")

# ... rest of your code for calculating plane cost and total holiday cost ...

#define a function to calculate ticket price
# def plane_cost(flight_cost, ticket_prices):  
#   if flight_cost in ticket_prices:
#     return ticket_prices[flight_cost]
#   else:
#     print("There is no ticket available for your selected destination, please select another one.")
#     return None  

flight_price = input("Please select one of these destinations: Tokyo, Bangkok, Seoul: ")

if flight_price in available_ticket_prices:
    ticket_price = available_ticket_prices[flight_price]
    print(input(f"Your flight price to{flight_price} is: {ticket_price}"))
else:
    print("The selected destination is not available,select another one")
# x = flight_price

# while True:
#   print(f"Your flight cost is: {plane_cost(flight_price, Available_tickets_price)}")
#   break  
# else:
#   print(x)
  

total_cost_of_holiday = (hotel_cost(num_nights, price_per_night) + car_rental(rental_cost_per_day, rental_days) + ticket_price(flight_price, Available_tickets_price))

print(f"Your holiday total cost will be: ", (total_cost_of_holiday))