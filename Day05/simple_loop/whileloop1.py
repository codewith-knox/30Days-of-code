#My Code


# while True:       #code repeat until conditions get false
#     number = int(input("what is your number: "))
#     if number == -1:       
#         break               #break commands exits the loop
#     print(number **2)

# print("Thanks and Bye!")



# Text book code 
#number = int(input("Please type in a number, -1 to quit: ")) # Infinite loop
while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break

    print(number ** 2)

print("Thanks and bye!")