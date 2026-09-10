# course Sample code

height = 172.5
weight = 68.55

# the Body Mass Index, or BMI, is calculated by dividing body mass with the square of height
# height is converted into metres in the formula
bmi = weight / (height / 100) ** 2

print(f"The BMI is {bmi}")

# // & /

x= 3
y= 2
print(f"/ operator {x/y}")
print(f"// operator {x//y}")

# Number as a input

year= int(input("Which year were you born? "))           #Integer
print(f"Your age at the end of the year 2027: {2027 -year}")

height = float(input("What is your height? "))          #Float
weight = float(input("What is your weight? "))

height = height / 100
bmi = weight / height ** 2

print(f"The BMI is {bmi}")

# Using Variables
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

sum = number1 + number2 + number3
print(f"The sum of the numbers: {sum}")