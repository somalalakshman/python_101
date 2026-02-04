"""
You are traveling from Hyderabad to Anantapur, distance is 300 kms.
you need 100 liters of fuel for the trip.
Ask user for current fuel in the vehicle (in liters).
If fuel is sufficient, print "You can start your journey"
If fuel is insufficient, print "You need X more liters to start your journey"
"""
total_fuel_needed = 100
user_current_fuel_input = input("Enter current fuel in the vehicle: ")
current_fuel = int(user_current_fuel_input)

is_fuel_sufficient = current_fuel > total_fuel_needed


if is_fuel_sufficient:
    print("You can start your journey")
else:
    fuel_required = total_fuel_needed - current_fuel
    print(f"You need {fuel_required} more liters to start your journey")