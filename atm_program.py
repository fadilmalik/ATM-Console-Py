import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Pin number: "))
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
        