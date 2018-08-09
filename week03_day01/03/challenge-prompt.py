
#Character One

# Make a variable called character_one_name and have it equal a string of Mr. Farley;
character_one_name = "Mr. Farley"

# Assign a new value, Ms. Farley, to the variable character_one_name.
character_one_name = "Ms. Farley"


# Now give character one a age
character_one_age = 2

# Make a variable called character_two_age and have it equal to a integer of 5 ;
character_two_age = 5


# Assign a new value, 6, to the varibale character_two_age.
character_two_age = 6


# Make a variable called character_one_salary and have it equal to 100000.00 ;
character_one_salary = 100000.00


# Make a variable called character_one_profession and have it equal to "Web Developer"
character_one_profession = "Web Developer"

# Make a variable called character_one_species and have it equal to "cat"
character_one_species = "cat"

# Make a variable called character_one_location and have it equal to "San Francisco CA"
character_one_location = "San Francisco CA"

# Make a variable called character_one_rent and have it equal to "2000.00"
character_one_rent = 2000.00


# Make a variable called character_one_expenses and have it equal to "1500.00"
character_one_expenses = 1500.00


# Make a variable called character_one_yearly_rent and have it equal to character_one_yearly_rent + 12
character_one_yearly_rent = character_one_rent * 12

# Make a variable called character_one_yealy_expenses and have it equal to 1500.00 * 12
character_one_yearly_expenses = 1500.00 * 12

# Make a variable called character_one_savings and have it equal to character_one_yearly_rent + character_one_yealy_expenses
character_one_savings = character_one_yearly_rent + character_one_yearly_expenses

#character Two
# Make a variable of charcter_two_name equal to a string of "Mr. Snuggles"
character_two_name = "Mr. Snuggles"

# Make a variable of character_two_age equal to a age of 3
character_two_age = 3

# Now redefine character_two_age to 4
character_two_age = 4

# Make a variable called character_two_species and have it equal to "mouse"
character_two_species = "mouse"

# Make a variable called character_two_salary and have it equal to 
character_two_salary = 1000.00

# Make a variable called character_two_location and have it equal to "Oakland, CA"
character_two_location = "Oakland, CA"

# Make a variable called character_two_rent and have it equal to "4000.00"
character_two_rent = 4000.00

# Make a variable called character_two_expenses and have it equal to "500.00"
character_two_expenses = 500.00

# Make a variable called character_two_yearly_rent and have it equal to character_two_yearly_rent + 12
character_two_yearly_rent = character_two_rent * 12

# Make a variable called character_two_yealy_expenses and have it equal to 1500.00 * 12
character_two_yearly_expenses = 1500.00 * 12

# Make a variable called character_two_savings and have it equal to character_two_yearly_rent + character_two_yealy_expenses
character_two_savings = character_two_yearly_rent + character_two_yearly_expenses

character_two_Profession = "Accountant"

#conditionals

# Write if statement to check if character_one_name is equal to "Mr. Farley"
if (character_one_name == "Mr. Farley"):
    # if it does == Mr. Farley then print a string of "Hello Mr. Farley"
    print("Hello Mr. Farley")
    # write a else if and check if character_one_name == "Ms. Farley"
elif (character_one_name == "Ms. Farley"):
    # if it does == Ms. Farley then print a string of "Hello Ms. Farley"
    print("Hello Ms. Farley")
    # finally if they both dont apply else
else:
    # print a string of "Hello stranger"
    print("Hello stranger")


# Write an if statement to check if character_two_age greater than character_two_age
if (character_two_age > character_one_age):
    # if character_two_age is greater than character_two_age then print a string of "Mr. Farley"
    print("Mr. Farley")
    # else print a string of "Ms. Farley"
else:
    print("Ms. Farley")



# Write an if statement to check if character_one_location is equal to "Oakland"
if (character_one_location == "Oakland"):
    # if character_one_location is equal to oakland print a string of "Raiders"
    print("Raiders")
    # else if character_two_location is equal to a string of "San Francisco" 
elif (character_two_location == "San Francisco"):
    #  print a string of Niners
    print("Niners")
    # if both condition doesn't apply write an else with a print a string of "Warriors"
else:
    print("Warriors")


# Write an if statement to check if character_one_rent greater than character_two_rent
if (character_one_rent > character_two_rent):
    # print a string of character_one_name with character_one_rent
    print(f"{character_one_name} pays ${character_one_rent} for rent")
    # else
else:
    # print a string of character_two_name with character_two_rent
    print(f"{character_two_name} pays ${character_two_rent} for rent")


# Write an if statement to check if character_one_expenses greater than character_two_expenses
if (character_one_expenses > character_two_expenses):
    # print a string of character_one_name with character_one_expenses
    print(f"{character_one_name}'s monthly expenses are ${character_one_expenses}")
    # else
else:
    # print a string of character_two_name with character_two_expenses
    print(f"{character_two_name}'s monthly expenses are ${character_two_expenses}")


# Write if statement to check if character_one_profession equal to a string of "Web Developer" and character_two_Profession is a string of "Accountant"
if (character_one_profession == "Web Developer" and character_two_Profession == "Accountant"):
    # print a string of "Look a Web Developer and a Accountant"
    print("Look a Web Developer and an Accoutant")
# else if character_one_profession and character_two_Profession doesn't equal those strings then
elif (character_one_profession != character_two_Profession):
    # print a string of "They're professionals."
    print("They're professionals")

