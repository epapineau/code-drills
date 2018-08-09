
# Declare a variable welcome_name as an `input` with a string of "Welcome to the sandwich shop, what do i call you?"
welcome_name = input("Welcome to the sandwich shop, what do i call you? ")
# Then print with a string of "Hello" and the varible of welcome_name
print(f"Hello {welcome_name}")

# Declare a variable question_sandwich as an `input` with a string of "Are you here for a sandwich?"
question_sandwich = bool(input("Are you here for a sandwich? "))
# If question_sandwich is equal to true
if (question_sandwich == True):
    # Declare a variable food_prompt as an `input` with a string of "What kind of sandwich would you like?"
    food_prompt = input("What kind of sandwich would you like? ")
    # Then print a string of "Please wait 10 min for your " with another variable of food_prompt
    print(f"Please wait 10 min for your {food_prompt}")
    # If question_sandwich isn't true print a string of "If you don't want a sandwich what are you here for?!"
else:
    print("If you don't want a sandwich what are you here for?!")