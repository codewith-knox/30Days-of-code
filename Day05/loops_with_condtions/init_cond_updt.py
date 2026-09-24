attempts =0        #Initialisation
while attempts <= 3:     #condtion
    passwd = input("Enter Your Pass: ")
    attempts +=1        #Updation

    if passwd =="4321":
        login = True
        break
    if attempts ==3:
        login = False
        break
    print("please try again...")

if login:
    print("You sucessfully login")
else:
    print("Too many attempts")    