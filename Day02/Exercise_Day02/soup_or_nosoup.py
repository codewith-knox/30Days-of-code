# Programming exercise:
# Soup or no soup

# Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

# Two examples of the program's execution:

# Sample output
# Please tell me your name: Kramer
# How many portions of soup? 2
# The total cost is 11.8
# Next please!
# Sample output
# Please tell me your name: Jerry
# Next please!


name = str(input("Please tell me your name: "))     #str use to typecast input as string

if name=="Jerry":
    print("Next please!")
else:
    portion_of_soup = int(input("How many portions of soup? ")) 
    total_cost = portion_of_soup*5.90
    print(f"The total cost is {total_cost}")
    print("Next please!")


# Book solution 
name = input("Please tell me your name:  ")
if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    cost = 5.9 * portions
    print("The total cost is", cost)
print("Next please!")
 