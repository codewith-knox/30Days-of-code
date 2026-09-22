# Programming exercise:
# Grades and points
# Points:

# The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

# points	grade
# < 0	impossible!
# 0-49	fail
# 50-59	1
# 60-69	2
# 70-79	3
# 80-89	4
# 90-100	5
# > 100	impossible!
# Some examples:

# Sample output
# How many points [0-100]: 37
# Grade: fail
# Sample output
# How many points [0-100]: 76
# Grade: 3
# Sample output
# How many points [0-100]: -3
# Grade: impossible!


grades = int(input("How many points [0-100]: "))
if grades > 100 or grades <0:
    print("Grade: impossible!")
elif grades >= 90 and grades <=100:
    print("Grade: 5")
elif grades >= 80 and grades <=89:
    print("Grade: 4")
elif grades >= 70 and grades <=79:
    print("Grade: 3")
elif grades >= 60 and grades <=69:
    print("Grade: 2")
elif grades >= 50 and grades <=59:
    print("Grade: 1")
elif grades >=0 and grades <=49:
    print("Grade: fail")
else:
    print("Grade: Impossible!")

