# Day 05
# Activity 05
import string

# This is our password strength checker function. 
# Refer to the README.md for instructions on the behavior.

# Define a function called check_strength that takes in a string called password.
def check_strength(password):
#------------- Start of function. ----------#

  # We've provided predefined set of valid alphabet and numbers
  # string.ascii_letters is a built in python method that is a string of all valid letters
  # string.digits is a built in python method that is a string of all valid numbers
  # learn more at https://docs.python.org/3.1/library/string.html

  alphabet = string.ascii_letters
  numbers = string.digits

  # create a boolean variable called weak_password to check if fewer than 6 characters then True.
  if(len(password) < 6):
    weak_password = True
  else:
    weak_password = False
    # declare and set two variables called contains_number and contains_letter as False
  contains_number = False
  contains_letter = False

  # Loop through each character in password and update contains_number or contains_letter
    # if there is a number then update contains_number to true
    # if there is a letter then update contains_letter to true
  for i in password:
    if(i in numbers):
      contains_number = True
    if(i in alphabet):
      contains_letter = True

  # Create an if statement for the following:
    # Very weak password contains equal to or fewer than 6 characters and consists only of numbers
      # Print "Your password is too weak."
  if(weak_password):
    print("Your password is too weak.")

    # Else if a very strong password containing more than 6 characters and consists of at least one number, at least one letter
      # Print "Average strength."
  elif(contains_letter and contains_number):
    print("Strong password")

    # Else print "Strong password"
  else:
    print("Average strength")
#------------- End of function. ----------#


# Declare a variable as user_input_password with an input stating "Please enter a password."
user_input_password = input("Please enter a password: ")
# Initiate the check_strength function with the user_input_password
check_strength(user_input_password)