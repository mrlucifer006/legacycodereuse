from support import *

def admin_menu():
    if not login("admin.csv"):
        print("Access denied")
        return
    while True:
        choice = input("Admin: 1 staff 2 add 3 update 4 delete 5 view 0 exit: ")
        if choice == "1": add_staff()
        elif choice == "2": add_food()
        elif choice == "3": update_food()
        elif choice == "4": delete_food()
        elif choice == "5": view_food()
        elif choice == "0": return

def staff_menu():
    if not login("delivery_staff.csv"):
        print("Access denied")
        return
    while True:
        choice = input("Staff: 1 add 2 update 3 view 0 exit: ")
        if choice == "1": add_food()
        elif choice == "2": update_food()
        elif choice == "3": view_food()
        elif choice == "0": return

def main():
    while True:
        choice = input("Food orders: 1 admin 2 delivery staff 3 customer 0 exit: ")
        if choice == "1": admin_menu()
        elif choice == "2": staff_menu()
        elif choice == "3": customer_order()
        elif choice == "0": break

if __name__ == "__main__":
    main()
