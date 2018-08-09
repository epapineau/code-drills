# import the necessary modules for reading csv files
import os
import csv

# prompt the user for a number from 1-807
pokemon = input("Which pokemon would you like to select? 1 - 807 ")

# set the path for the csv file
csvpath = os.path.join("..", "Resources", "pokemon.csv")

# create new lists to store data for heaviest and tallest pokemon
heaviest = []
tallest = []

# open the csv
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # remember to exclude the header when iterating through the data
    csv_header = next(csvreader)

    # iterate through the data and search for the number the user inputed
    for row in csvreader:
        if(row[0] == pokemon):
            # print the name of the pokemon(identifier) and pokedex number(species id) at that number. 
            # eg. "Pokemon No. 25 - pikachu"
            print(f"Pokemon No. {row[0]} - {row[1]}")
        
        # iterate through the data and search for pokemon whose weight is greater than 3000
        # append only the pokemon's name and weight to the 'heaviest' list
        if(int(row[4]) > 3000):
            heaviest.append(f"{row[1]} - {row[4]}kg")

         # iterate through the data and search for pokemon whose height is greater than 50
         # append only the pokemon's name and height to the 'tallest' list
        if(int(row[3]) > 50):
            tallest.append(f"{row[1]} - {row[3]}m")


# print the list of heaviest and tallest pokemon
print(heaviest)
print("---------------------------------")
print(tallest)