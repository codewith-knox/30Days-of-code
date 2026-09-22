# example 01 and logical operator
number = int(input("Please type in a number: "))
if number >= 5 and number <= 8:             #both condtion must be true
    print("The number is between 5 and 8")




# example 02 or logical operator
number = int(input("Please type in a number: "))
if number < 5 or number > 8:                           #either one is true
    print("The number is not within the range of 5 to 8")


# Exammple 03
number = int(input("Please type in a number: "))
if not (number >= 5 and number <= 8):
    print("The number is not within the range of 5 to 8")


