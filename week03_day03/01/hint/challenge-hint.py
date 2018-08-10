# declare a variable called user_input_list and set it to an empty list for now
user_input_list = []
# create a string of all the valid_inputs for our validation logic to check against user's input
valid_inputs = ["*", "/", "+", "-"]

# ==================== Evaluation Function ====================

# Feel free to come back to this function later if you want to.
# We will not be using this immediately.

# Define a function that takes in user_input_list to check the operator's sign
def calculator(user_input_list):
  # if the operator is a '+' sign, return the value of the first number added to the second number
  if("+" in user_input_list):
    input_split = user_input_list.split("+")
    num1 = int(input_split[0])
    num2 = int(input_split[1])
    return num1 + num2
  # else if the operator is a '-' sign, return the value of the first number subtracted from the second number
  elif("-" in user_input_list):
    input_split = user_input_list.split("-")
    num1 = int(input_split[0])
    num2 = int(input_split[1])
    return num1 - num2
  # else if the operator is a '*' sign, return the value of the first number multiplied by the second number
  elif("*" in user_input_list):
    input_split = user_input_list.split("*")
    num1 = int(input_split[0])
    num2 = int(input_split[1])
    return num1 * num2
  # else if the operator is a '/' sign, return the value of the first number divided by the second number
  else:
    input_split = user_input_list.split("/")
    num1 = int(input_split[0])
    num2 = int(input_split[1])
    return num1 / num2

#
# =============================================================

user_input_list = input("Please input a calculation: ")
print(user_input_list)

# Declare For each of the following 3 variables, one for the first number, one for the second, and one for the operator.
confirmed_input = False
while (confirmed_input == False):
  for i in user_input_list:
    print(i)
    # if user_input is in list of valid_inputs
    if(i in valid_inputs):
      # Then append user_input to user_input_list
      confirmed_input = True
    else:
      # print "User input is not a valid input."
      print("User input is not a valid input")

# Declare a variable called calculator_result set it to the function defined in the previous step.
calculator_result = calculator(user_input_list)
# Print the user's equation requested by concatenating the user_input_list and the value of calculator_result.
print(f"{user_input_list} = {calculator_result}")
# Output example: 1 + 3 = 4