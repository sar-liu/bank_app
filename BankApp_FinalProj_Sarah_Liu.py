#programmer: Sarah Liu
#description: Final project "Bank App"- simulate a banking application.
#date: 12/10/23

def deposit(depAmount):
    prevBal= float(balance[userIndex])
    newBal = prevBal + depAmount
    balance[userIndex]= newBal
    
def withdraw(withAmount):
    prevBal= float(balance[userIndex])
    newBal = prevBal - withAmount
    balance[userIndex]= newBal
    
def showBalance():
    print("Current balance: $")
    print(balance[userIndex])
    
def changeUser():
    validUser=False

    while validUser==False:
        accountUser= input("Enter your username: ")    
        accountPass= input("Enter your password: ")
        
        if (accountUser in userName)==True:
            userIndex= userName.index(accountUser)
            if (accountPass == passWord[userIndex]):
                print("Logged in.\n")
                validUser=True
                return userIndex
                
            else:
                print("Invalid password.\n")
           
        else:
            print('Invalid username.\n')  
def addClient():
    print("Welcome, new user!")
    newUser= input("Enter your username: ")    
    newPass= input("Enter your password: ")
    newBal= input("Enter your balance: $")
    userName.append(newUser)
    passWord.append(newPass)
    balance.append(newBal)
    
    print("\nCurrent accounts:")
    print(userName)
    print(passWord)
    print(balance)
def end():
    userInfo.close()
    outFile= open('UserInformtion.txt', 'w')
    for i in range(len(userName)):
        outFile.write(str(userName[i]))
        outFile.write(" ")
        outFile.write(str(passWord[i]))
        outFile.write(" ")
        outFile.write(str(balance [i]))
        outFile.write("\n")
    exit()
    
#############################################

userInfo = open('UserInformtion.txt', 'r')
userName = []
passWord= []
balance= []
    
for line in userInfo: 
    values = line.split() 
    userName.append(values[0])
    passWord.append(values[1])
    balance.append(values[2])
  

# print(userName)
# print(passWord)
# print(balance)
repeat=True
userIndex=changeUser()

while repeat==True:
    print("-----------------------------------------")
    print("Hello", userName[userIndex],"!")
    showBalance()
    print("\nType D to deposit money\nType W to withdraw money\nType B to display Balance\nType C to change user, display user name\nType A to add new client\nType E to exit") 
    option= input("Please select an option: ")
    
    if option =="d" or option == "D":
        depAmount=float(input("Enter the amount to deposit: $"))
        deposit(depAmount)
        showBalance()
    elif option =='w' or option == 'W':
        showBalance()
        withAmount=float(input("Enter the amount to withdraw: $"))
        
        if withAmount <= float(balance[userIndex]):
            withdraw(withAmount)
            showBalance()
        else:
            print("Error: Not enough balance.\n")
        
    elif option=='b' or option == 'B':
        showBalance()
    elif option=='c' or option == 'C':
        userIndex= changeUser()
    elif option =='a' or option == 'A':
        addClient()
    elif option == 'e' or option == 'E':
        end()
    else:
        print("Error: Choose one of the options above.\n")

  