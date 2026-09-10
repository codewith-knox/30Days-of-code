# Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.

# The program should function as follows:

# Sample output
# How many days? 1
# Seconds in that many days: 86400
# Another example:

# Sample output
# How many days? 7
# Seconds in that many days: 604800


while True:                             # looping to rerun after usser get ans  #extra
    days = int(input("How many days? "))
    result = (days*24*60*60)       #in a each day  24hour , in a each hour 60 min , in a each min 60 sec
    print(f"Seconds in that many days: {result}")
