print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("whats is your age ? "))
    bill = 0
    if age <= 12:
        print("childen ticket is for5$")
        bill = 5
    elif age <= 18 :
         print("youth ticket is for 7$")
         bill = 7
    else: print(" adult ticket is for 10$")
    bill = 10
    wants_photo = input("Do you want a photo taken? Type y for yes or n for no. ")
    if wants_photo == 'y':
        bill += 3
        print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")
