print("\n🎈Hello let's select your vehicle and type🎈.")

print("\nWhich vehicle will you select ?\n1. Car🚗\n2. Bike🛵")
choice = int(input("Enter the ride number : "))

if (choice == 2):
    print("\nWhich bike will you select ?\n1. Scooter🛴 \n2. Scooty🛵")
    choice2 = int(input("Enter the ride number : "))
    if (choice2 == 1):
        print("You have selected scooter🛴 . Have fun !")
    else:
        print("You have selected scooty🛵 . Have fun !")

elif (choice == 1):
    print("\nWhich car will you select ?\n1. Sedan🚗 \n2. XUV🚗")
    choice3 = int(input("Enter the ride number : "))
    if (choice3 == 1):
        print("You have selected sedan🚗 . Have fun !")
    else:
        print("You have selected XUV🚗 . Have fun !")

else:
    print(" This is not a correct number / invalid number ❌.  Please enter a valid number .\n")

