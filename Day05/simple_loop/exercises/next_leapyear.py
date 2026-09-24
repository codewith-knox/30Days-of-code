# Programming exercise:
# The next leap year

# Please write a program which asks the user for a year, and prints out the next leap year.

# Sample output
# Year: 2023
# The next leap year after 2023 is 2024
# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

# Sample output
# Year: 2024
# The next leap year after 2024 is 2028
# year = int(input("Year: "))

# year = int(input("Year: "))
# attempts =0
# while True:
#     year = int(input("Year: "))
   
#     if year % 4 ==0:
#         leap_year = True
#         break
#     # elif year+attempts % 4 ==0:
#     #     leap_year = False
#     #     break
    
        

# if leap_year:
#     print(f"The next leap year after {year} is {year+4}")




# if year % 4 ==0:
#     if year % 100 ==0:
#         if year % 400==0:
#             print("That year is a leap year.")
#         else:
#             print("That year is not a leap year.")
#     else:
#         print("That year is a leap year.")
# else:
#     print("That year is not a leap year.")

    
attempts =0
while True:
    year = int(input("Year: "))
    attempts +=1
    new_year = year + attempts
   
    # if year % 4 ==0:
    #     leap_year = True
    #     break
    # if year % 4 ==0:
    #     if year % 100 ==0:
    #         if year % 400==0:
    
    # elif new_year % 4 ==0:
    #      leap_year = False
    #      break
    
        

if leap_year:
    print(f"The next leap year after {year} is {year+4}")
else:
    print(f"The next leap year after {year} is {year + attempts}")



