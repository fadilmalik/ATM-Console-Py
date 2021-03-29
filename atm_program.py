import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Enter your pin number: "))
    trial = 0

    while(id != int(atm.checkPin()) and trial < 3):
        id = int(input("Wrong pin number. Try again: "))
        
        trial +=1 

        if trial == 3:
            print("Error! Take a card and Try again..")
            exit()

    while True:
        print("Welcome to ATM Console")
        print("1. Balance Check \n2. Withdraw \n3. Deposit \n4. Change Pin \n5. Exit")

        selectMenu = int(input("Select Menu: "))
        if selectMenu == 1:
            print("\nYour current balance: Rp. " +
            str(atm.checkBalance()) + "\n")

        elif selectMenu == 2:
            nomina = float(input("Enter the balance amount: "))
            verify_withdraw = input(
                "Confirmation: \nYou will make a withdrawal with the following amount ?\n" +
                str(nomina) + "\nPlease select: y/n" + "\n")

            if verify_withdraw == "y":
                    print("Your previous balance: Rp. " +
                            str(atm.checkBalance()) + "\n")
            else:
                break
            if nomina < atm.checkBalance():
                    atm.withdraw(nomina)
                    print("Balance withdrawal is successful")
                    print("Your current balance:Rp. " + str(atm.checkBalance()))
            else:
                    print("Sorry, your balance is not enough to make a withdrawal")
                    print("Please make a deposit first")

        elif selectMenu == 3:
            nomina = float(input("Enter the balance amount: "))
            verify_deposit = input(
                "Confirmation: You will deposit the following amount ?\n" + 
                str(nomina) + "\nPlease select: y/n" + "\n")
            
            if verify_deposit == "y":
                atm.deposit(nomina)
                print("Balance deposit is successful")
                print("Your current balance: Rp. " +
                        str(atm.checkBalance()) + "\n")
            else:
                break

        elif selectMenu == 4:
            verify_pin = int(input("Enter your pin number: "))

            while verify_pin != int(atm.checkPin()):
                print("The pin you entered is wrong, please try again")
                break

            update_pin = int(input("Enter new pin number: "))
            print("Pin changed successfully")

            verify_newpin = int(input("Re-enter new pin number: "))

            if verify_newpin == update_pin:
                print("The new pin has been successfully verified")
            else:
                print("The pin number you entered is wrong")

        elif selectMenu == 5:
            print("Receipt is printed automatically when you leave. \nPlease save this receipt as proof of your transaction.")
            print("-" * 20)
            print("Record Number: ", random.randint(100000, 1000000))
            print("Date: ", datetime.datetime.now())
            print("-" * 20)
            print("Thank you for using the atm console.")
            exit()
        else:
            print("Error. the menu you selected does not exist!")