# Programming exercise:
# Alphabetically in the middle
# Points:

# Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, or all lowercase.

# Some examples of expected behaviour:

# Sample output
# 1st letter: x
# 2nd letter: c
# 3rd letter: p
# The letter in the middle is p
# Sample output
# 1st letter: C
# 2nd letter: B
# 3rd letter: A
# The letter in the middle is B

l1= str(input("1st letter :"))
l2= str(input("2nd letter :"))
l3= str(input("3rd letter :"))

if l2 > l1 and l2<l3:
    print(f"The letter in the middle is {l2}")
