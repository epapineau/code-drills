# define a function "warble" that takes in a string as an argument,
# adds " arglebargle" to the end of it, and returns the result
def warble(string):
    return(f"{string} arglebargle")

# print the result of calling your "warble" function with the argument "hello"
warble("hello")


# define a function "wibble" that takes a string as an argument,
# prints the argument, prepends "wibbly " to the argument, and returns the result
def wibble(string):
    return(f"wibbly {string}")

# print the result of calling your "wibble" function with the argument "bibbly"
wibble("bibbly")


# define a function "print_sum" that takes in two numbers as arguments
# and prints the sum of those two numbers
def print_sum(num1, num2):
    sum = num1 + num2
    print(sum)



# testing your function - un-comment the following two lines when you have finished your function

print("The following should be 5")
print_sum(2, 3)

# define a function "return_sum" that takes in two numbers as arguments
# and returns the sum of those two numbers
def return_sum(num1, num2):
    sum = num1 + num2
    return sum



# testing your function - un-comment the following two lines when you have finished your function

print("The following should be 12")
print(return_sum(5, 7))

# using either "return_sum" and no mathematical operators,
# define a function "triple_sum" that takes in 3 arguments and returns the sum of those 3 numbers
def triple_sum(num1, num2, num3):
    hold = return_sum(num1, num2)
    sum = return_sum(hold, num3)
    return sum

# testing your function - un-comment the following two lines when you have finished your function

print("The following should be 16")
print(triple_sum(2, 6, 8))



# define a function "dance_party" that takes in a string as an argument,
# that prints "dance!",
# updates the string from calling "wibble" function with that argument,
# updates the string from calling "warble" function with that argument,
# returns the updated string
def dance_party(string):
    print("dance!")
    print(string)
    print(warble(wibble(string)))



# print the result of calling your "dance_party" function with your name as the argument
dance_party("Elize")

# Should result in:
# dance!
# MyName
# wibbly MyName arglebargle

