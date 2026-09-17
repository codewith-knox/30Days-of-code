# print() is use to display output on the console


print("Row, row, row your boat,\n" + "Gently down the stream.\n" + "Merrily, merrily, merrily, merrily,\n" + "Life is but a dream.")  
print(type("python \n"+"3"))  #type() is used to check data types
print(3)
print("@")


name= input("What is your name? ")               #name,email,nickname are varaibles that store data and use in future
email = input("What is your email address? ")
nickname = input("What is your nickname? ")

print("Let's make sure we got this right")
print("Your name: " + name)
print("Your email address: " + email)           # '+'is used to concatenate two string
print("Your nickname: " + nickname)

part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-"+part2+"-"+part3)

num =3
ver="3.14@"
print(f"python{num}\nversion: {ver}")
