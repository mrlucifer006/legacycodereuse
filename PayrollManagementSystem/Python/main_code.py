# import necessary modules
import support as m1
import time, os
import pandas as pd

'''The admin() function allows adminstrators to manage the systems by performing various tasks that include adding new 
HRs, adding new payroll data, updating existing payroll data, deleting payroll data and viewing all payroll data'''

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
            print("1.Add HR\n2.Add Payroll Data\n3.Update Payroll Data\n4.Delete Payroll Data\n5.View Payroll Data\n6.Exit")
            # Gets admin's choice
            choice = int(input("Enter your choice (1/2/3/4/5/6) : "))
            # Handle admin's choice
            match choice:
                case 1:
                    # Add a new HR
                    os.system('cls')
                    new_user = input("Enter the new ID :")
                    new_pass = input("Enter the new Password :")
                    m1.add_hr(new_user, new_pass)
                    print("The HR is added successfully !")
                    time.sleep(2)
                    m1.view_hrs()
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Add a new payroll
                    os.system('cls')
                    name = input("Payroll Category : ")
                    price = int(input("Amount : "))
                    m1.add_data(name, price)
                    print("The payroll data has been added to the list !")
                    ch = input("Do you want to continue (y/n)? ")
                case 3:
                    # Update an existing payroll
                    os.system('cls')
                    name = input("Enter the payroll category : ")
                    price = int(input("Enter the altered amount : "))
                    m1.update_data(name, price)
                    print("The payroll amount has been modified successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 4:
                    # Delete a payroll
                    os.system('cls')
                    name = input("Enter the payroll category to be removed : ")
                    m1.del_data(name)
                    print("The payroll data has been removed successfully !")
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    # View all payrolls
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

'''The hr() function allows HRs to manage payroll data by performing tasks such as adding new payroll data, updating 
existing payroll data, viewing all payroll data'''
def hr():
    # Get HR credentials
    uid = input("Enter your user id : ")
    pas = input("Enter your password : ")
    # Verify HR credentials
    result = m1.check_hr(uid, pas)
    if result == "verified" or True:
        # Display success message
        print("HR login successful !")
        # Loop until HR chooses to exit
        ch = "y"
        while ch.lower() == "y":
            os.system('cls')
            # Get HR choice
            print("1.Add Payroll Data\n2.Update Payroll Data\n3.View Payroll Data\n4.Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))
            # Handle HR's choice
            match choice:
                case 1:
                    # Add a new payroll
                    os.system('cls')
                    name = input("Enter payroll category: ")
                    price = int(input("Enter payroll amount: "))
                    m1.add_data(name, price)
                    print("Payroll data has been added successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 2:
                    # update an existing payroll
                    os.system('cls')
                    name = input("Enter the payroll category to be updated: ")
                    price = int(input("Enter amount to be updated: "))
                    m1.update_data(name, price)
                    print("Payroll data has been updated successfully !")
                    ch = input("Do you want to continue(y/n)? ")
                case 3:
                    # View all payrolls
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

'''The employee() function simulates an employee experience and allow employees to view available claims,add claims 
to their requests,view their requests and proceed to confirm claims'''

def employee():
    # Welcome message for employee
    print("Welcome, Employee!")
    # Intialize a variable to track user's choice to continue
    ch = "y"
    # Initialize an empty requests
    requests = []
    # Initialize total price and tax
    total_price = 0
    tax = 0
    # Loop until user chooses to exit
    while ch.lower() == "y":
        # clear the console
        os.system('cls')
        # Display menu options
        print("1. View Available Claims\n2. Request Claim\n3. View Requests\n4. Confirm Claims\n5. Exit")
        try:
            # Get users choice
            choice = int(input("Enter your choice (1/2/3/4/5): "))
            # Use match statement to handle different choices
            match choice:
                # Handle view claims option
                case 1:
                    # Clear the console
                    os.system('cls')
                    # Display claims
                    m1.display_data()
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user idf they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 2:
                    # Clear the console
                    os.system('cls')
                    # Prompt user to enter item numbers to add to requests
                    print("Enter claim numbers to request (enter -1 to finish):")
                    # Display the claims
                    m1.display_data()
                    # Loop until user finishes requesting items
                    while True:
                        # Get item number from the user
                        try:
                            num = int(input("Enter the claim number: "))
                            # Check if user wants to finish adding items
                            if num != -1:
                                pass
                            else:
                                # Break out of the loop
                                break
                            # Read payroll.csv file
                            df = pd.read_csv("payroll.csv",index_col=0)
                            # Check if the item number is valid
                            if num in df.index:
                                # Get item name and price
                                item_name = df.loc[num, "category"]
                                item_price = df.loc[num, "amount"]
                                # Add item to requests
                                requests.append((item_name, num, item_price))
                                # Update total price
                                total_price += item_price
                                # Print conformation message
                                print(f"Added {item_name} to requests!")
                            else:
                                # Print error message for invalid item number
                                print("Invalid claim number.")
                        except ValueError:
                            # print error message for invalid input
                            print("Please enter a valid number.")
                    # print requests total
                    print(f"Requests total: {total_price}")
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")

                # Handle view requests option
                case 3:
                    # clear the console
                    os.system('cls')
                    # Check if the requests is empty
                    if not requests:
                        # print message the requests is empty
                        print("Your request list is empty.")
                    else:
                        # print requests contents
                        print("Your Requests:")
                        for item in requests:
                            # Print each item in the requests
                            print(f"Claim {item[0]}: {item[1]} - ₹{item[2]}")
                        # Print total price
                        print(f"Total: {total_price}")
                    # Pause execution for 5 seconds
                    time.sleep(5)
                    # Ask user if they want to continue
                    ch = input("Do you want to continue (y/n)? ")
                case 5:
                    #Print thankyou message for the employee
                    print("Thank you for using the system!")
                    break
                case 4:
                    #Clear the console
                    os.system('cls')
                    # Check if requests is empty
                    if not requests:
                        print("Your request list is empty. Please request claims before proceeding.")
                    else:
                        # Print billing summary
                        print("=== Claim Summary ===")
                        for item in requests:
                            print(f"Claim {item[1]} - ₹{item[2]}")
                        tax = total_price * 0.1
                        print("="*40)
                        print(f"Total Amount : ₹{total_price}")
                        print(f"Deductions : ₹{tax}")
                        print(f"Final payout : ₹{total_price - tax}")
                        # Ask user to confirm request
                        confirm = input("Confirm claim requests (y/n)? ")
                        if confirm.lower() == "y":
                            # Print successful message
                            print("Request successful! Your claims are being processed!")
                        else:
                            print("Request cancelled.")
                        # Reset requests and total price
                        requests = []
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
            print("An automated payroll management software".center(170))
            # Get the user type from user
            print("1.Admin\n2.HR\n3.Employee\n4.Exit")
            user_type = int(input("Enter user type(1/2/3/4): "))
            # Use match statement to handle different user types
            match user_type:
                case 1:
                    # Clear console and call admin function
                    os.system("cls")
                    admin()
                case 2:
                    # Clear console and call HR function
                    os.system("cls")
                    hr()
                case 3:
                    # Clear the console and call employee function
                    os.system("cls")
                    employee()
                    print("Thank you for using our service.")
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
