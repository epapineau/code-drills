# declare a variable named our_list and assign an empty list to it
our_list = []

# we can `append` values into an list with the append method. Documentation can be found here:
# https://www.w3schools.com/python/ref_list_append.asp

# Let's append the number 1 into our_list
our_list.append(1)


# append the string "hello" into our_list
our_list.append("hello")

# append the boolean false into our_list
our_list.append(False)

# append the number 84 into our_list
our_list.append(84)

# append the string "world" into our list
our_list.append("world")

# print our_list
print(our_list)


# This seperator is here to make your prints are little easier to read 
# by creating seperations between the different sections of the activity
print("--------------------------Seperator 1--------------------------")

# declare a variable named one_to_ten and assign it an list containing the numbers from 1 to 10
one_to_ten = range(1, 11)

# print the element at index 4
print(one_to_ten[4])


# print the element at index 7
print(one_to_ten[7])




# This seperator is here to make your prints a little easier to read 
# by creating seperations between the different sections of the activity
print("--------------------------Seperator 2--------------------------")

# We've declared this list for you
num_list = [2, 65, 3, 7, 39, 22, 11, 94, 299, 9, 20, 21, 51, 37]
# iterate through num_list and create an individual print for every number greater than 50
for i in num_list:
  if(i > 50):
    print(i)

    
# iterate through num_list and print the index of the first occurance for the number 11
for i in num_list:
  if(i == 11):
    print(num_list.index(i))
    break


# iterate through num_list and print the sum of all the numbers
total = 0
for i in num_list:
  total = total + i
print(total)
  
# iterate through num_list and print the sum of all the numbers greater than 50
total = 0
for i in num_list:
  if(i > 50):
    total = total + i
print(total)


# iterate through num_list and print the sum of all the even numbers
total = 0
for i in num_list:
  if(i % 2 == 0):
    total = total + i
print(total)


# This seperator is here to make your prints a little easier to read 
# by creating seperations between the different sections of the activity
print("--------------------------Seperator 3--------------------------")

# We've declared this list for you
fruits = [
  "Apple", "Orange", "Banana", "Pomelo", "Apple", "Kiwi", "Peach", "Banana", "Grape", "Tomato", 
  "Kiwi", "Apple", "Watermelon", "Lemon", "Pomelo", "Apple", "Banana", "Peach", "Apricot", "Grape"]
# iterate through fruits and print the number of times "Apple" appears in the list
total = 0
for i in fruits:
  if (i == "Apple"):
    total = total + 1
print(total)


# iterate through fruits and print the number of times "Peach" appears in the list
total = 0
for i in fruits:
  if (i == "Peach"):
    total = total + 1
print(total)


# iterate through fruits and print the number of fruits that start with "P" in the list
total = 0
for i in fruits:
  if(i[0] == "P"):
    total = total + 1
print(total)


# CHALLENGE (Optional!) 
# create a new empty list named unique_fruits
unique_fruits = []

# iterate through fruits and populate unique_fruits with only unique values from fruits
# you should a shorter list without repeated values. (Hint: try looking up "not in" conditionals for if statements)
for i in fruits:
  if(i not in unique_fruits):
    unique_fruits.append(i)


# print out your unique_fruits list
print(unique_fruits)


# CHALLENGE (Optional!)
# This seperator is here to make your prints a little easier to read 
# by creating seperations between the different sections of the activity
print("--------------------------Seperator 4--------------------------")


# In this challenge we're going to be working with nested lists. 
# You can store any type of data within an list- even other lists!
two_dim_list = [
  [54, 6, 7, 46, 78],
  [43, 9, 6, 65, 65],
  [32, 1, 44, 1, 23],
  [55, 12, 2, 34, 2],
  [2, 12, 44, 2, 12]]

# another seperator for your convenience
print("======== first list ========")
# iterate through the first list inside two_dim_list and print all the numbers less than 25
for i in two_dim_list[0]:
  if(i < 25):
    print(i)


# another seperator for your convenience
print("======== second list ========")
# iterate through the second list inside two_dim_list and print all the numbers less than 25

for i in two_dim_list[1]:
  if(i < 25):
    print(i)

# another seperator for your convenience
print("======== fifth list ========")
# iterate through the fifth list inside two_dim_list and print all the numbers less than 25
for i in two_dim_list[4]:
  if(i < 25):
    print(i)


# another seperator for your convenience
print("======== odd numbers ========")
# iterate through two_dim_list and the lists inside of it and print all the odd numbers
for i in range(len(two_dim_list)):
  for u in two_dim_list[i]:
    if(u % 2 == 1):
      print(u)


# another seperator for your convenience
print("======== sum of multiples of 3 ========")
# iterate through two_dim_list and the lists inside of it and 
# print the sum of all the numbers that are a multiple of 3
total = 0
for i in range(len(two_dim_list)):
  for u in two_dim_list[i]:
    if(u % 3 == 0):
      total = total + 1
print(total)