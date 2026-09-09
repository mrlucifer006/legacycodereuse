# import necessary modules
import support as m1
import time, os
import pandas as pd

'''The admin() function allows adminstrators to manage the systems by performing various tasks that include adding new 
receptionists, adding new rooms, updating existing room prices, deleting rooms and viewing all rooms'''

def admin():
    # Get admin credentials
    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")
    # Verify admin credentials
    result = m1.check_admin(uid, pas)
    if result == "verified":
        # Loop until admin chooses to exit
        ch = "y"
        while ch.lower() == "y":
            # Clear the screen and display admin menu
            os.system('cls')
            print("1.Add Receptionist\n2.Add Room Data\n3.Update Room Data\n4.Delete Room Data\n5.View Room Data\n6.Exit")
            # Gets admin's choice
            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))
            # Handle admin's choice
            match choice:
                case 1:
                    # Add a new receptionist
                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_receptionist(new_user, new_pass)
                    print("The receptionist is added successfully !")
                    time.sleep(2)
                    m1.view_receptionists()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Add a new room
                    os.system('cls')
                    name = input("Room Type : ")
                    price = int(input("Price : "))
                    m1.add_data(name, price)
                    print("The room has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:
                    # Update an existing room
                    os.system('cls')
                    name = input("Enter the room type : ")
                    price = int(input("Enter the altered price : "))
                    m1.update_data(name, price)
                    print("The room price has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:
                    # Delete a room
                    os.system('cls')
                    name = input("Enter the room type to be removed : ")
                    m1.del_data(name)
                    print("The room has been removed successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    # View all rooms
                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue (y/n)? ")
                case 6:
                    # Exit admin menu
                    print("Exited successfully !")
                    break
                case _:
                    # Handle invalid input
                    print("Invalid input")
                    break
    else:
        # Display error message for invalid credentials
        print("Invalid username or password")
        time.sleep(2)

'''The receptionist() function allows receptionists to manage rooms by performing tasks such as adding new rooms, updating 
existing room prices, viewing all rooms'''
def receptionist():
    # Get receptionist credentials
    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")
    # Verify receptionist credentials
    result = m1.check_receptionist(uid, pas)
    if result == "verified" or True:
        # Display success message
        print("Receptionist login successful !")
        # Loop until receptionist chooses to exit
        ch = "y"
        while ch.lower() == "y":
            os.system('cls')
            # Get receptionist choice
            print("1.Add Room\n2.Update Room\n3.View Rooms\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))
            # Handle receptionist's choice
            match choice:
                case 1:
                    # Add a new room
                    os.system('cls')
                    name = input("Enter room type: ")
                    price = int(input("Enter room price: "))
                    m1.add_data(name, price)
                    print("Room has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:
                    # update an existing room
                    os.system('cls')
                    name = input("Enter the room type to be updated: ")
                    price = int(input("Enter price to be updated: "))
                    m1.update_data(name, price)
                    print("Room has been updated successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 3:
                    # View all rooms
                    os.system('cls')
                    m1.display_data()
                    time.sleep(5)
                    os.system('cls')
                    ch = input("Do you want to continue(y/n)? ")
                case 4:
                    #To exit the option
                    print("Exited successfully !")
                    break
                case _:
                    # Handle invalid input for user type
                    print("Invalid input")
                    # Break out of the loop
                    break
    else:
        # Print error messsage for invalid username or password
        print("Invalid username or password")
        # Pause execution for 2 seconds
        time.sleep(2)

'''The customer() function simulates booking experience and allow customers to view available rooms,add rooms 
to their booking,view their booking and proceed to billing'''

def customer():
    # Welcome message for customer
    print("Welcome, Customer!")
    # Intialize a variable to track user's choice to continue
    ch = "y"
    # Initialize an empty booking
    booking = []
    # Initialize total price and discount
    total_price = 0
    discount = 0
    # Loop until user chooses to exit
    while ch.lower() == "y":
        # clear the console
        os.system('cls')
        # Display menu options
        print("1. View Rooms\n2. Book Room\n3. View Booking\n4. Checkout\n5. Exit")
        try:
            # Get users choice
            choice = int(input("Enter your choice (1/2/3/4/5): "))
            # Use match statement to handle different choices
            match choice:
                # Handle view rooms option
                case 1:
                    # Clear the console
                    os.system('cls')
                    # Display rooms
                    m1.display_data()
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user idf they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Clear the console
                    os.system('cls')
                    # Prompt user to enter item numbers to add to booking
                    print("Enter room numbers to book (enter -1 to finish):")
                    # Display the rooms
                    m1.display_data()
                    # Loop until user finishes booking items
                    while True:
                        # Get item number from the user
                        try:
                            num = int(input("Enter the room number: "))
                            # Check if user wants to finish adding items
                            if num != -1:
                                pass
                            else:
                                # Break out of the loop
                                break
                            # Read rooms.csv file
                            df = pd.read_csv("rooms.csv",index_col=0)
                            # Check if the item number is valid
                            if num in df.index:
                                # Get item name and price
                                item_name = df.loc[num, "room_type"]
                                item_price = df.loc[num, "price"]
                                # Add item to booking
                                booking.append((item_name, num, item_price))
                                # Update total price
                                total_price += item_price
                                # Print conformation message
                                print(f"Added {item_name} to booking!")
                            else:
                                # Print error message for invalid item number
                                print("Invalid room number.")
                        except ValueError:
                            # print error message for invalid input
                            print("Please enter a valid number.")
                    # print booking total
                    print(f"Booking total: {total_price}")
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")

                # Handle view booking option
                case 3:
                    # clear the console
                    os.system('cls')
                    # Check if the booking is empty
                    if not booking:
                        # print message the booking is empty
                        print("Your booking is empty.")
                    else:
                        # print booking contents
                        print("Your Booking:")
                        for item in booking:
                            # Print each item in the booking
                            print(f"Room {item[0]}: {item[1]} - ₹{item[2]}")
                        # Print total price
                        print(f"Total: {total_price}")
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    #Print thankyou message for the customer
                    print("Thank you for using our service!")
                    break
                case 4:
                    #Clear the console
                    os.system('cls')
                    # Check if booking is empty
                    if not booking:
                        print("Your booking is empty. Please book rooms before proceeding to checkout.")
                    else:
                        # Print billing summary
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
                        # Ask user to confirm checkout
                        confirm = input("Confirm checkout (y/n)? ")
                        if confirm.lower() == "y":
                            # Print successful message
                            print("Checkout successful! Thank you for staying with us!")
                        else:
                            print("Checkout cancelled.")
                        # Reset booking and total price
                        booking = []
                        total_price = 0

                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask if the user want to continue
                    ch = input("Do you want to continue (y/n)? ")
                # Handle invalid input
                case _:
                    # Print eror message
                    print("Invalid input")
                    # Ask if they want to continue
                    ch = input("Do you want to continue (y/n)? ")
        except ValueError:
            # Printing the error message
            print("Please enter a valid number.")
            # Ask the user if they want to continue
            ch = input("Do you want to continue (y/n)? ")

'''The main() function serves as the entry point of the software and it displays a menu to select user
 type, calls the corresponding function based on user input, handles invalid inputs and exceptions and asks the user if they 
 want to continue using the software'''
def main():
    ch = 'y'
    # Loop until user chooses to exit
    while ch.lower() == "y":
        try:
            #Clear the console
            os.system('cls')
            # Display title and menu
            print("An automated hotel management software".center(170))
            # Get the user type from user
            print("1.Admin\n2.Receptionist\n3.Customer\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))
            # Use match statement to handle different user types
            match user_type:
                case 1:
                    # Clear console and call admin function
                    os.system("cls")
                    admin()
                case 2:
                    # Clear console and call receptionist function
                    os.system("cls")
                    receptionist()
                case 3:
                    # Clear the console and call customer function
                    os.system("cls")
                    customer()
                    print("Thank you for using our service. Visit us again!")
                case 4:
                    # Clear the console and print exit message
                    os.system("cls")
                    print("Exited. Thank you for using our service".center(170))
                    break
                case _:
                    # Print the error message
                    print("Invalid input. Enter a valid choice.")
        # Handle value error exception
        except ValueError:
            print("Please enter a valid number.")
            # Ask the user if they want to continue
            ch = input("Do you want to continue (y/n)? ")

#Check if the script is being run directly
if __name__ == "__main__":
    main()
