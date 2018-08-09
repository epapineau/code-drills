# Declare a variable of boba_shop  with an input and a string of "Welcome to the Boba Shop!"
boba_shop = input("Welcome to the Boba Shop! ")
# Check if boba_shop  is equal to true
if (bool(boba_shop) == True):
    
    # Write a print with a string of "Hello"
    print("Hello")

    # Declare a variable of beverage with an input and a string of "What kind of boba drink would you like ?"
    beverage = input("What kind of boba drink would you like? ")

    # Declare a variable of sweetness with an input and a string of "How sweet do you want your drink 0,50,100,200 ?"
    sweetness = int(input("How sweet do you want your drink - 0, 50, 100, or 200? "))
    # Now check 
    # if sweetness equals to 50 print "half sweetened"
    if(sweetness == 50):
        print("half sweetened")
    # else if sweetness 100 print "normal sweet"
    elif(sweetness == 100):
        print("normal sweet")

    
    # else if sweetness 200 print "super sweet"
    elif(sweetness == 200):
        print("super sweet")

    # else print with a string of "non-sweet"
    else:
        print("non-sweet")


    # then print with a string of "your order of " variable beverage and a string of " boba with a sweet level of " and variable of sweetness
    print(f"Your order of {beverage} boba with a sweet level of {sweetness}")
    # and print string of "goodbye".
    print("Goodbye")

