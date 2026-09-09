import support

def main():
    print("Welcome to Hotel Management System")
    print("1. Admin\n2. Receptionist\n3. Customer\n4. Exit")
    try:
        choice = int(input("Choose role: "))
        if choice == 1:
            support.admin_menu()
        elif choice == 2:
            support.receptionist_menu()
        elif choice == 3:
            support.customer_menu()
        elif choice == 4:
            return
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
