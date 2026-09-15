from support import *

def admin_rooms():
    if not login("admin.csv"):
        print("Access denied")
        return
    while True:
        choice = input("Admin: 1 staff 2 add 3 update 4 delete 5 view 0 exit: ")
        if choice == "1": add_staff()
        elif choice == "2": add_room()
        elif choice == "3": update_room()
        elif choice == "4": delete_room()
        elif choice == "5": view_room()
        elif choice == "0": return

def staff_rooms():
    if not login("receptionist.csv"):
        print("Access denied")
        return
    while True:
        choice = input("Staff: 1 add 2 update 3 view 0 exit: ")
        if choice == "1": add_room()
        elif choice == "2": update_room()
        elif choice == "3": view_room()
        elif choice == "0": return

def main():
    while True:
        choice = input("Room orders: 1 admin 2 receptionist 3 customer 0 exit: ")
        if choice == "1": admin_rooms()
        elif choice == "2": staff_rooms()
        elif choice == "3": customer_order()
        elif choice == "0": break

if __name__ == "__main__":
    main()
