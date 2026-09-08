# varaibles stores data in the memory
# var = val     in left side there is varname and right side its value
# Changing the variable:
var="var1"
var="var2"
var=var+"\nchanges" # when u assigned new value to the variables old assigned value is replaced with new one
print(var)

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f'- {skill1} ({level1})')
print(f'- {skill2} ({level2})')
print(f'- {skill3} ({level3})\n')
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")




# Book solution.  

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000
 
print(f"my name is {name}, I am {age} years old")
print("")
print("my skills are")
print(" -", skill1, "("+level1+")")
print(" -", skill2, "("+level2+")")
print(" -", skill3, "("+level3+")")
print("")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

# print("- ",skill1, " (", level1, ")")
# print("- ",skill2, " (", level2, ")")
# print("- ",skill3, " (", level3, " )")





# # print("aryan","gupta")

# # print("-",skill1,)
# print(f'- {skill1} ({level1})')

# print(" (",skill1,")")