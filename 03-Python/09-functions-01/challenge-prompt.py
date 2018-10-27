# define a function "fun" that prints "Functions are FUN!"
def fun():
    print("Functions are FUN!")

# define a function "thirty_seven" that prints the sum of 18 and 19
def thirty_seven():
    print(18 + 19)

# call two functions you've defined so far
fun()
thirty_seven()


# define a function "log" that takes in a parameter and prints that parameter
def log(parameter):
    print(parameter)
# define a function "hello" that calls on the "log" function to print "Hello World"
def hello():
    log("Hello World")

# call your "hello" function
hello()

# define a function "user_input" that asks the user for their name and stores it in a variable called "user_name"
# print the user's name
def user_input():
    user_name = input("What is your name? ")
    print(user_name)


# call your "user_input" function
user_input()


# define a function "good_day" that creates a confirm dialogue asking the user if they are having a nice day
# and then print the response using the log function you made earlier
def good_day():
    day = input("Are you having a good day? ")
    log(day)

# call your "good_day" function
good_day()


# define a function "favorite_fruit" that prompts the user for their favorite fruit
# and then print the response using the log function you made earlier
def favorite_fruit():
    fruit = input("What is your favorite fruit? ")
    log(fruit)
# call your "favorite_fruit" function
favorite_fruit()