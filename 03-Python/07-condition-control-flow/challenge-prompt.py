# Create a variable called 'farm'
# set that farm variable to be a list with the elements
# pig, cow, chicken, dog, horse, sheep
farm = ["pig", "cow", "chicken", "dog", "horse", "sheep"]

# Write an if statement that prints the string "RWAR!" if the first element of farm is not "Godzilla"
if(farm[0] != "Godzilla"):
    print("RWAR!")

# Write another if statement that prints the string "SCREECH!" if the last element of farm is "Mothra"
if(farm[len(farm) - 1] == "Mothra"):
    print("SCREECH!")

# Declare a variable named 'dog' with a string of "Spot"
dog = "Spot"

# declare 3 variables cat, city, car without assigning them values
cat = ""
city = ""
car = ""

# assign the string "Farley" to cat
cat = "Farley"

# assign the string "San Francisco" to city
city = "San Francisco"

# assign the string "Prius" to car
car = "Prius"

# using string concatenation, print out the sentence 
# "See Spot run!" without explicitly using "Spot" inside the string.
print(f"See {dog} run!")

# using string concatenation, print out the sentence 
#"I drive Farley around San Francisco in my Prius" without explicityly 
#using "Farley", "San Francisco", and "Prius"
# Remember to use the variables we just declared!
print(f"I drive {cat} around {city} in my {car}")

# declare a variable budget and assign it a value of 5000
budget = 5000

# declare a variable rent_cost and assign it a value of 1500
rent_cost = 1500

# declare a variable utilities_cost and assign it a value of 150
utilities_cost = 150

# declare a variable food_cost and assign it a value of 250
food_cost = 250

# declare a variable transportation_cost and assign it a value of 350
transportation_cost = 350

# declare a variable computer_cost and assign it a value of 2000
computer_cost = 2000

# Declare a variable called total_cost that takes the sum of all costs above (excluding budget).
total_cost = rent_cost + utilities_cost + food_cost + transportation_cost + computer_cost

# write an if statement that checks whether the sum of all our costs is within the budget.
# if it is within budget, print "You're total cost is " with the total cost, 
# otherwise, print "You're over budget by " difference of budget vs total cost.
if (total_cost < budget):
    print(f"You're total cost is {total_cost}")
else:
    print(f"You're over budget by ${total_cost - budget}")


# write an if statement that checks whether the rent_cost is larger than 
# the sum of the utilities_cost, food_cost, and transportation_cost
# and if computer_cost is greater than the sum of rent_cost and utilities_cost
# if both those statements are true, print a string that says "This computer is too expensive!"
# else,print a string that says "Rent is too damn high!"

sum1 = utilities_cost + food_cost + transportation_cost
if(rent_cost > sum1 and computer_cost > (rent_cost + utilities_cost)):
    print("This computer is too expensive!")
else:
    print("Rent is too damn high!")