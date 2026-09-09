
import support as m1
import time, os
import pandas as pd

def admin():

    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")

    result = m1.check_admin(uid, pas)
    if result == "verified":

        ch = "y"
        while ch.lower() == "y":

            os.system('cls')
            print("1.Add Receptionist\n2.Add Room Data\n3.Update Room Data\n4.Delete Room Data\n5.View Room Data\n6.Exit")

            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))

            match choice:
                case 1:

                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_receptionist(new_user, new_pass)
                    print("The receptionist is added successfully !")
                    time.sleep(2)
                    m1.view_receptionists()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:

                    os.system('cls')
                    name = input("Room Type : ")
                    price = int(input("Price : "))
                    m1.add_data(name, price)
                    print("The room has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:

                    os.system('cls')
                    name = input("Enter the room type : ")
                    price = int(input("Enter the altered price : "))
                    m1.update_data(name, price)
                    print("The room price has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:

                    os.system('cls')
                    name = input("Enter the room type to be removed : ")
                    m1.del_data(name)
                    print("The room has been removed successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 5:

                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue (y/n)? ")
                case 6:

                    print("Exited successfully !")
                    break
                case _:

                    print("Invalid input")
                    break
    else:

        print("Invalid username or password")
        time.sleep(2)

def receptionist():

    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")

    result = m1.check_receptionist(uid, pas)
    if result == "verified" or True:

        print("Receptionist login successful !")

        ch = "y"
        while ch.lower() == "y":
            os.system('cls')

            print("1.Add Room\n2.Update Room\n3.View Rooms\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))

            match choice:
                case 1:

                    os.system('cls')
                    name = input("Enter room type: ")
                    price = int(input("Enter room price: "))
                    m1.add_data(name, price)
                    print("Room has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:

                    os.system('cls')
                    name = input("Enter the room type to be updated: ")
                    price = int(input("Enter price to be updated: "))
                    m1.update_data(name, price)
                    print("Room has been updated successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 3:

                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue(y/n)? ")
                case 4:

                    print("Exited successfully !")
                    break
                case _:

                    print("Invalid input")

                    break
    else:

        print("Invalid username or password")

        time.sleep(2)

def customer():

    print("Welcome, Customer!")

    ch = "y"

    booking = []

    total_price = 0
    discount = 0

    while ch.lower() == "y":

        os.system('cls')

        print("1. View Rooms\n2. Book Room\n3. View Booking\n4. Checkout\n5. Exit")
        try:

            choice = int(input("Enter your choice (1/2/3/4/5): "))

            match choice:

                case 1:

                    os.system('cls')

                    m1.display_data()

                    time.sleep(5)

                    ch = input("Do you want to continue (y/n)? ")
                case 2:

                    os.system('cls')

                    print("Enter room numbers to book (enter -1 to finish):")

                    m1.display_data()

                    while True:

                        try:
                            num = int(input("Enter the room number: "))

                            if num != -1:
                                pass
                            else:

                                break

                            df = pd.read_csv("rooms.csv",index_col=0)

                            if num in df.index:

                                item_name = df.loc[num, "room_type"]
                                item_price = df.loc[num, "price"]

                                booking.append((item_name, num, item_price))

                                total_price += item_price

                                print(f"Added {item_name} to booking!")
                            else:

                                print("Invalid room number.")
                        except ValueError:

                            print("Please enter a valid number.")

                    print(f"Booking total: {total_price}")

                    ch = input("Do you want to continue (y/n)? ")

                case 3:

                    os.system('cls')

                    if not booking:

                        print("Your booking is empty.")
                    else:

                        print("Your Booking:")
                        for item in booking:

                            print(f"Room {item[0]}: {item[1]} - ₹{item[2]}")

                        print(f"Total: {total_price}")

                    time.sleep(5)

                    ch = input("Do you want to continue (y/n)? ")
                case 5:

                    print("Thank you for using our service!")
                    break
                case 4:

                    os.system('cls')

                    if not booking:
                        print("Your booking is empty. Please book rooms before proceeding to checkout.")
                    else:

                        print("=== Billing Summary ===")
                        for item in booking:
                            print(f"Room {item[1]} - ₹{item[2]}")
                        tax = total_price * 0.18
                        if total_price > 5000:
                            discount = total_price * 0.1
                        print("="*40)
                        print(f"Total Price : ₹{total_price}")
                        print(f"Tax : ₹{tax}")
                        print(f"Discount : ₹{discount}")
                        print(f"Final price : ₹{total_price + tax - discount}")

                        confirm = input("Confirm checkout (y/n)? ")
                        if confirm.lower() == "y":

                            print("Checkout successful! Thank you for staying with us!")
                        else:
                            print("Checkout cancelled.")

                        booking = []
                        total_price = 0

                    time.sleep(5)

                    ch = input("Do you want to continue (y/n)? ")

                case _:

                    print("Invalid input")

                    ch = input("Do you want to continue (y/n)? ")
        except ValueError:

            print("Please enter a valid number.")

            ch = input("Do you want to continue (y/n)? ")

def main():
    ch = 'y'

    while ch.lower() == "y":
        try:

            os.system('cls')

            print("An automated hotel management software".center(170))

            print("1.Admin\n2.Receptionist\n3.Customer\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))

            match user_type:
                case 1:

                    os.system("cls")
                    admin()
                case 2:

                    os.system("cls")
                    receptionist()
                case 3:

                    os.system("cls")
                    customer()
                    print("Thank you for using our service. Visit us again!")
                case 4:

                    os.system("cls")
                    print("Exited. Thank you for using our service".center(170))
                    break
                case _:

                    print("Invalid input. Enter a valid choice.")

        except ValueError:
            print("Please enter a valid number.")

            ch = input("Do you want to continue (y/n)? ")

if __name__ == "__main__":
    main()
