# while True:
#     a = 5
#     b = int(input("Number: "))
#     if a > b:
#         print("A is greater than B")

attempt =0
while True:
    password=input("Please Enter Your password: ")
    attempt +=1
    #if password == password:     #potential bug while programming
    if password == "1234":     
        sucess = True
        break
    if attempt ==3:
        sucess = False
        break
    print("Please Try again...")

if sucess:
    print("You sucessfully loged in")
else:
    print("Uff Too many Try....")   


attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if attempts == 3:
        success = False
        break

    if code == "1234":
        success = True
        break

    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")



while True:
    print("beginning of the while block:")
    code = input("Please type in your PIN: ")
    attempts += 1

    print("attempts:", attempts)
    print("condition1:", attempts == 3)
    if attempts == 3:
        success = False
        break

    print("code:", code)
    print("condition2:", code == "1234")
    if code == "1234":
        success = True
        break

    print("Incorrect...try again")