import support

def main():
    print("Welcome to Payroll Management System")
    print("1. Admin\n2. HR\n3. Employee\n4. Exit")
    try:
        choice = int(input("Choose role: "))
        if choice == 1:
            support.admin_menu()
        elif choice == 2:
            support.hr_menu()
        elif choice == 3:
            support.employee_menu()
        elif choice == 4:
            return
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
